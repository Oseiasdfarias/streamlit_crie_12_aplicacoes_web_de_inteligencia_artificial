import streamlit as st
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot as plt
from datetime import date
from io import StringIO
import seaborn as sns


# Define o estilo Seaborn
sns.set_style("ticks")

pg_title = "Sistema de Análise e previsão de Séries Temporais"
st.set_page_config(page_title=pg_title, layout="wide")

# st.title(pg_title)

new_title = f'<h1 style="font-family:sans-serif; color:Cyan; font-size: 30px;">{pg_title}</h1>'  # noqa: E501
st.markdown(new_title, unsafe_allow_html=True)

with st.sidebar:
    uploarded_file = st.file_uploader("Escolha o arquivo:", type=["csv"])
    if uploarded_file is not None:
        stringio = StringIO(uploarded_file.getvalue().decode("utf-8"))
        data = pd.read_csv(stringio, header=None)
        data_inicio = date(2000, 1, 1)
        periodo = st.date_input("Período inicial da Série", data_inicio)
        periodo_precisao = st.number_input("Informe quantos meses quer prever",
                                           min_value=1, max_value=48)
        processar = st.button("Processar")


if uploarded_file is not None and processar:
    try:
        ts_data = pd.Series(data.iloc[:, 0].values,
                            index=pd.date_range(
                                start=periodo,
                                periods=len(data),
                                freq="M"
                            ))
        decomposicao = seasonal_decompose(ts_data, model="additive")
        fig_decomposicao = decomposicao.plot()
        fig_decomposicao.set_size_inches(12, 8)
        sns.despine()

        modelo = SARIMAX(ts_data, order=(2, 0, 0),
                         seasonal_order=(0, 1, 1, 12))
        modelo_fit = modelo.fit()
        previsao = modelo_fit.forecast(steps=periodo_precisao)

        fig_previsao, ax = plt.subplots(figsize=(12, 5))
        ax = ts_data.plot(ax=ax)
        previsao.plot(ax=ax, style="r--")
        sns.despine(offset=10, trim=True)

        col1, col3 = st.columns([7, 4])
        with col1:
            st.write("Decomposição da Série")
            st.pyplot(fig_decomposicao)
            if periodo_precisao > 1:
                st.write(f"Previsão do Modelo para {periodo_precisao} meses")
            else:
                st.write(f"Previsão do Modelo para {periodo_precisao} mês")
            st.pyplot(fig_previsao)
        with col3:
            if periodo_precisao > 1:
                st.write(f"Dados da Previsão para {periodo_precisao} meses")
            else:
                st.write(f"Dados da Previsão para {periodo_precisao} mês")
            st.dataframe(previsao)

    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
