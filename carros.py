import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Classificação Veículos",
    layout="wide"
)


@st.cache_data
def load_data_and_model():
    carros = pd.read_csv("car.csv", sep=",")
    encoder = OrdinalEncoder()

    for col in carros.columns.drop("class"):
        carros[col] = carros[col].astype("category")

    X_encoded = (encoder
                 .fit_transform(
                     carros.drop("class", axis=1)
                    ))
    y = carros["class"].astype("category").cat.codes

    X_train, X_test, y_train, y_test = (
        train_test_split(X_encoded, y,
                         test_size=0.3,
                         random_state=42)
    )

    modelo = CategoricalNB()

    # trainamdo o modelo
    modelo.fit(X_train, y_train)

    # Avaliando o modelo trainado
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)

    return encoder, modelo, acuracia, carros


encoder, modelo, acuracia, carros = load_data_and_model()

st.title("Previsão de Qualidade de Veículo")
st.write(f"Acurácia do Modelo: {(acuracia*100):.0f}%")

# SelectBox dos atributos para passa para o modelo
st.header("Selecione os atributos do veículo!")
input_features = [
    st.selectbox("Preço: ", carros["buying"].unique()),
    st.selectbox("Manutenção: ", carros["maint"].unique()),
    st.selectbox("Portas: ", carros["doors"].unique()),
    st.selectbox("Capacidade de Passageiros: ", carros["persons"].unique()),
    st.selectbox("Porta Malas: ", carros["lug_boot"].unique()),
    st.selectbox("Segurança do Veículo: ", carros["safety"].unique()),
    ]
st.markdown("#### **Clique no Botão para realizar a previsão**")

unacc = """
            **unacc (Inaceitável):** O algorítimo classificou
            o veículo como ***Inaceitável***."""
acc = """
            **acc (Aceitável):** O algorítimo classificou o veículo
            como ***Aceitável***."""
good = """
           **good (Bom):** O algorítimo classificou
           o veículo como ***Bom***."""
vgood = """
            **vgood (Muito Bom):** O algorítimo classificou o veículo
            como ***Muito Bom***."""

if st.button("Processar"):
    input_df = pd.DataFrame(
        [input_features],
        columns=carros.columns.drop("class"))
    input_encoded = encoder.transform(input_df)

    predict_encoded = modelo.predict(input_encoded)
    predict_decoder = (carros["class"]
                       .astype("category")
                       .cat
                       .categories
                       [predict_encoded][0])

    st.markdown("---")
    if predict_decoder == "unacc":
        st.header(f":red[Resultado da Previsão: {predict_decoder}]")
        st.markdown(f":orange[{unacc}]")
    elif (predict_decoder == "acc"):
        st.header(f":red[Resultado da Previsão: {predict_decoder}]")
        st.markdown(f":orange[{acc}]")
    elif (predict_decoder == "good"):
        st.header(f":green[Resultado da Previsão: {predict_decoder}]")
        st.markdown(f":orange[{good}]")
    elif (predict_decoder == "vgood"):
        st.header(f":green[Resultado da Previsão: {predict_decoder}]")
        st.markdown(f":orange[{vgood}]")

st.markdown("---")

st.markdown("### **Descrição do Problema de Negócio**")

descricao_pn = """
 A empresa ***Car 24H*** oferece serviços de assistência 24 horas e enfrenta
 um desafio relacionado à precificação de seus serviços, devido à variação
 na frequência de problemas entre os veículos devido a características
 distintas. Para lidar com essa questão, a empresa necessita de um sistema
 que utilize dados históricos, como manutenção regular do veículo, quantidade
 de portas, capacidade de passageiros e segurança do veículo, para prever
 a qualidade de cada veículo. Com essa previsão de qualidade, a empresa
 poderá precificar de forma mais precisa seus serviços, ajustando os preços
 de acordo com o potencial de ocorrência de problemas em cada veículo.
"""
st.markdown(descricao_pn)

st.markdown("---")

st.markdown("### **Descrição do Projeto**")

descricao = """O Projeto visa solucionar o problema de negócio da empresa
            ***Car 24H*** a partir de um sistema que avalie e preveja a
            qualidade dos veículos baseando-se em características históricas,
            utilizando algoritmos de classificação. Foi usando o algorítimo
            Classificador Naive Bayes.
"""
st.markdown(descricao)


nb_descricao = """
    O classificador Naive Bayes é um algoritmo de aprendizado de máquina
    baseado no teorema de Bayes, que presume independência entre os recursos
    (variáveis) do conjunto de dados. Na biblioteca scikit-learn (sklearn) do
    Python, você pode usar o Naive Bayes através do módulo
    `sklearn.naive_bayes`. Este módulo oferece várias implementações do
    classificador Naive Bayes,
    incluindo:
    - CategoricalNB (Usado no Projeto)
    - Gaussian Naive Bayes
    - Multinomial Naive Bayes
    - Bernoulli Naive Bayes

"""

st.markdown(nb_descricao)


st.markdown("---")


st.markdown("### **Código do Projeto**")

code = """

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Classificação Veículos",
    layout="wide"
)


@st.cache_data
def load_data_and_model():
    carros = pd.read_csv("car.csv", sep=",")
    encoder = OrdinalEncoder()

    for col in carros.columns.drop("class"):
        carros[col] = carros[col].astype("category")

    X_encoded = (encoder
                 .fit_transform(
                     carros.drop("class", axis=1)
                    ))
    y = carros["class"].astype("category").cat.codes

    X_train, X_test, y_train, y_test = (
        train_test_split(X_encoded, y,
                         test_size=0.3,
                         random_state=42)
    )

    modelo = CategoricalNB()

    # trainamdo o modelo
    modelo.fit(X_train, y_train)

    # Avaliando o modelo trainado
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)

    return encoder, modelo, acuracia, carros


encoder, modelo, acuracia, carros = load_data_and_model()

st.title("Previsão de Qualidade de Veículo")
st.write(f"Acurácia do Modelo: {(acuracia*100):.0f}%")

# SelectBox dos atributos para passa para o modelo
st.header("Atributos do carro")
input_features = [
    st.selectbox("Preço: ", carros["buying"].unique()),
    st.selectbox("Manutenção: ", carros["maint"].unique()),
    st.selectbox("Portas: ", carros["doors"].unique()),
    st.selectbox("Capacidade de Passageiros: ", carros["persons"].unique()),
    st.selectbox("Porta Malas: ", carros["lug_boot"].unique()),
    st.selectbox("Segurança do Veículo: ", carros["safety"].unique()),
    ]

if st.button("Processar"):
    input_df = pd.DataFrame(
        [input_features],
        columns=carros.columns.drop("class"))
    input_encoded = encoder.transform(input_df)

    predict_encoded = modelo.predict(input_encoded)
    predict_decoder = (carros["class"]
                       .astype("category")
                       .cat
                       .categories
                       [predict_encoded][0])
    st.header(f"Resultado da Previsão: {predict_decoder}")



"""

st.code(f"""
    {code}
""")
