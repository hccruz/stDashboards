# Importar as bibliotecas
import streamlit as st
import pandas as pd
import collections
import plotly.express as px


# Importação/Manipulação dos dados
def importa_dado():
    df = pd.read_csv("data/vgsales.csv")
    df.dropna(inplace=True)
    df = df[df['Year'] <= 2016]
    df['Year'] = df['Year'].astype(int)
    plataformas = ['Wii', 'PS3', 'XOne', 'X360', 'PC', 'PS4']
    filtro = df['Platform'].isin(plataformas)
    return df[filtro]


df = importa_dado()

# Configuração Inicial

st.set_page_config(page_title="Dashboards Games", layout="wide")

st.markdown("<h1 style='text-align:center;'>📊Dashboards de Games</h1>",
            unsafe_allow_html=True)

st.divider()

# Sidebar

st.sidebar.title("Informe o Filtro Desejado")

plataforma = st.sidebar.multiselect(
    "Selecione a Plataforma",
    options=df["Platform"].unique(),
    default=df["Platform"].unique()
)

genero = st.sidebar.multiselect(
    "Selecione o Gênero",
    options=df["Genre"].unique(),
    default=df["Genre"].unique()
)

df_selecao = df.query(
    "Platform == @plataforma & Genre == @genero"
)

# Frequência de Vendas

freq_vendas = df_selecao.groupby('Year')\
                                .count()\
                                .sort_values('Name', ascending=False)\
                                .reset_index()[['Year', 'Name']]
top_10 = freq_vendas.head(10)
grafico01 = px.bar(top_10,
                   x='Year',
                   y='Name',
                   title='Frequência de Vendas',
                   labels={'Nome', 'Frequência'},
                   color_discrete_sequence=px.colors.sequential.Aggrnyl
                   )
grafico01

# 10 jogos mais frequentes

top_10_freq_jogos = pd.DataFrame(collections.Counter(
    df_selecao['Name'].tolist()).most_common(10),
    columns=['Game', 'Frequency']
)
grafico02 = px.bar(top_10_freq_jogos,
                   x='Game',
                   y='Frequency',
                   title='10 Jogos Mais Frequentes')
grafico02

# col1, col2 = st.columns(2)
# with col1:
#     grafico01
# with col2:
#     grafico02

# Melhores Jogos

coluna = ['NA_Sales']
titulo = ['North America']

for i, c in enumerate(coluna):
    df_vendas = df_selecao.groupby('Name')\
        .sum().sort_values(c, ascending=False)\
        .head(10).reset_index()[['Name', c]]
    grafico03 = px.bar(df_vendas,
                       x='Name',
                       y=c,
                       title=f'Os 10 Melhores Jogos {titulo[i]}',
                       labels={'Nome', 'Jogo'})
    grafico03

# Remove Estilo Streamlit
remove_st_estilo = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""

st.markdown(remove_st_estilo, unsafe_allow_html=True)
