import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score


class Classificador:
    def __init__(_self, path_data) -> None:
        _self.path_data = path_data
        _self.X_train, _self.X_test, _self.y_train, _self.y_test = (
            None, None, None, None)
        _self.encoder = OrdinalEncoder()
        _self.df_carros = None
        _self.load_data(_self.path_data)
        _self.pre_processamento_df()
        _self.encoder_and_split_df()

    @st.cache_data
    def load_data(_self, path_data):
        _self.df_carros = pd.read_csv(path_data)

    @st.cache_data
    def pre_processamento_df(_self):
        for col in _self.df_carros.columns.drop("class"):
            _self.df_carros[col] = _self.df_carros[col].astype("category")

    @st.cache_data
    def encoder_and_split_df(_self):
        X_encoded = (_self.encoder.fit_transform(
                        _self.df_carros.drop("class", axis=1)))
        y = _self.df_carros["class"].astype("category").cat.codes

        _self.X_train, _self.X_test, _self.y_train, _self.y_test = (
            train_test_split(X_encoded, y, test_size=0.3, random_state=42)
            )

    def classificador_nb(_self):
        modelo = CategoricalNB()
        # trainamdo o modelo
        modelo.fit(_self.X_train, _self.y_train)
        # Avaliando o modelo trainado
        _self.y_pred = modelo.predict(_self.X_test)
        acuracia = accuracy_score(_self.y_test, _self.y_pred)
        return _self.encoder, modelo, acuracia, _self.df_carros
