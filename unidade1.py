import pandas as pandas
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_database():
    return pd.read.csv('brasil_estados.csv')

st.title('Meu primeiro App - GCI')

estados = load_database();
st.dataframe(estados)

dados, estatistica = st.tabs(['Dados', 'Estatística Descritiva'])

with dados:
    regiao = st.selectbox(
        'Selecione a Região:',
        estados['regiao_nome'].unique()
    )
    st.dataframe(estados[estados['regiao_nome'] == regiao])