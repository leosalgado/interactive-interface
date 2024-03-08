import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("TDE - Pobreza e trabalho infantil")

pobreza = pd.read_csv("datasets/pobreza.csv", encoding="latin-1")
trabalho = pd.read_csv("datasets/trabalho.csv", encoding="latin-1")
trabalho_pobreza = pd.read_csv("datasets/trabalho_pobreza.csv", encoding="latin-1")

mes = st.sidebar.selectbox("Mês", trabalho_pobreza["MES REFERENCIA"].unique())

trabalho_pobreza_filtrado = trabalho_pobreza[trabalho_pobreza["MES REFERENCIA"] == mes]
trabalho_filtrado = trabalho[trabalho["MES REFERENCIA"] == mes]

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

linhas = len(trabalho_filtrado)

fig_situacao = px.pie(trabalho_filtrado, values='total', names='SITUACAO BENEFICIO', title="Situação dos benefícios")
col2.plotly_chart(fig_situacao, use_container_width=True)

fig_reg = px.bar(trabalho_filtrado, x='total', y='UF', title="Regiões que utilizaram o benefício")
col1.plotly_chart(fig_reg, use_container_width=True)

fig_tot_fam_pob = px.bar(trabalho_pobreza_filtrado, x="UF", y="cadunico_tot_fam_pob", title="Total de famílias em situação de pobreza")
col3.plotly_chart(fig_tot_fam_pob, use_container_width=True)

fig_tot_pes_pob = px.bar(trabalho_pobreza_filtrado, x="UF", y="cadunico_tot_pes_pob", title="Total de pessoas em situação de pobreza")
col4.plotly_chart(fig_tot_pes_pob, use_container_width=True)

fig_tot_fam_ext_pob = px.bar(trabalho_pobreza_filtrado, x="UF", y="cadunico_tot_fam_ext_pob", title="Total de famílias em situação de extrema pobreza")
col5.plotly_chart(fig_tot_fam_ext_pob, use_container_width=True)

fig_tot_pes_ext_pob = px.bar(trabalho_pobreza_filtrado, x="UF", y="cadunico_tot_fam_ext_pob", title="Total de pessoas em situação de extrema pobreza")
col6.plotly_chart(fig_tot_pes_ext_pob, use_container_width=True)
