import pandas as pd
import streamlit as st

regiao = pd.read_excel('BRCidadesRegiao.xlsx')

st.dataframe(regiao)