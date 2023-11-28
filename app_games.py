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
    return df


df = importa_dado()

# Configuração Inicial

st.set_page_config(page_title="Dashboards Games", layout="wide")

st.markdown("<h1 style='text-align:center;'>📊Dashboards de Games</h1>",
            unsafe_allow_html=True)

st.divider()

# Remove Estilo Streamlit
remove_st_estilo = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""

st.markdown(remove_st_estilo, unsafe_allow_html=True)
