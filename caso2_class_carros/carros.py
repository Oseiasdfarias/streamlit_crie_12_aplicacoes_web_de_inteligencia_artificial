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
                    )
                )
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
