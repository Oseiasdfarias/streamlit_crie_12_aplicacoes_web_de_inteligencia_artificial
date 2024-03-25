import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


st.title("Previsão Inicial de Custo para Franquia")

dados = pd.read_csv("./caso1_franquias/slr12.csv", sep=";")

X = dados[["FrqAnual"]]
y = dados["CusInic"]
modelo = LinearRegression().fit(X, y)

col1, col2 = st.columns(2)

with col1:
    st.header("Dados")
    st.table(dados.head(5))

with col2:
    st.header("Gráfico de Dispersão")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y, color="blue")
    ax.plot(X, modelo.predict(X), color="red")
    st.pyplot(fig)

st.header("Valor Anual da Franquia")
min_value = float(dados["FrqAnual"].min())
max_value = float(dados["FrqAnual"].max())
novo_valor = st.number_input(
    f"Insira novo valor entre {min_value:.2f} e {max_value:.2f}",
    min_value=min_value,
    max_value=max_value,
    value=float(dados["FrqAnual"].median()),
    step=0.01)
processar = st.button("Processar")

if processar:
    dados_novo_valor = pd.DataFrame(
        [[novo_valor]],
        columns=["FrqAnual"])
    prev = modelo.predict(dados_novo_valor)
    st.header(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")
