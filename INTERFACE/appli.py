import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor


# To run this app you must write in your terminal the following code : "streamlit run appli.py"

# import dataset

dataframe = pd.read_csv('df')

# Split datas

X = dataframe[['distance', 'price', 'volume_cm3']]
y = dataframe['freight_value']

# Création du model


# Apllication

st.set_page_config(
    page_title="predictions ",
    page_icon="🖥",
    layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# left bar

with st.sidebar:
    st.markdown("<h1 style='color: white;text-align: center; margin-bottom: 50px'>Choix du modèle</h1>",
                unsafe_allow_html=True)

    m_dropdown = st.selectbox('modèle', ['regression linéaire',
                                         'arbres de décision', 'gradient boosting'])

    slider = st.slider(
        'Pourcentage de données utilisé pour tester', 0, 100, 20)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=slider/100)

    st.write(slider/100)

    if m_dropdown == "regression linéaire":
        st.markdown("<h1 style='color: white;text-align: center; margin-bottom: 60px'>Type de regression </h1>",
                    unsafe_allow_html=True)

        r_dropdown = st.selectbox('modèle', ['Simple',
                                             'Lasso', 'Ridge', 'Elastic'])

# menu

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 50px'>Predictions</h1>",
            unsafe_allow_html=True)

container = st.container()

col1, col2 = st.columns(2)

## first section ##

with container:

    with col1:
        st.subheader('frais de transport')

        form = st.form(key="freight_value prediction_form")

        feature1 = form.number_input('distance')
        feature2 = form.number_input('price')
        feature3 = form.number_input('volume_cm3')
        button = form.form_submit_button("Predict")

        df = pd.DataFrame({'distance': [feature1], 'price': [
                          feature2], 'volume_cm3': [feature3]})

        scaler = StandardScaler()
        scaled = scaler.fit_transform(df[['distance', 'price', 'volume_cm3']])

        if button:
            try:
                if m_dropdown == "gradient boosting":
                    gradient = GradientBoostingRegressor()
                    gradient.fit(X_train, y_train)
                    pred = gradient.predict(scaled)
                    st.write("r2_score :", gradient.score(X_test, y_test))
                    st.write(pred)

                if r_dropdown == "Simple":
                    linear = LinearRegression()
                    linear.fit(X_train, y_train)
                    pred = linear.predict(scaled)
                    st.write(pred)
                    st.write("r2_score :", linear.score(X_test, y_test))
                    st.markdown(
                        "<p style='color: red'>Nous pouvons apercevoir que le résultat n'est pas représentatif des données rentrées</>", unsafe_allow_html=True)

                elif r_dropdown == "Lasso":
                    lasso = Lasso(alpha=0.1)
                    lasso.fit(X_train, y_train)
                    pred = lasso.predict(scaled)
                    st.write(pred)
                    st.markdown(
                        "<p style='color: red'>Nous pouvons apercevoir que le résultat n'est pas représentatif des données rentrées</>", unsafe_allow_html=True)

                elif r_dropdown == "Ridge":
                    ridge = Ridge(alpha=1)
                    ridge.fit(X_train, y_train)
                    pred = ridge.predict(scaled)
                    st.write(pred)
                    st.markdown(
                        "<p style='color: red'>Nous pouvons apercevoir que le résultat n'est pas représentatif des données rentrées</>", unsafe_allow_html=True)

                elif r_dropdown == 'Elastic':
                    elastic = ElasticNet()
                    elastic.fit(X_train, y_train)
                    pred = elastic.predict(scaled)
                    st.write(pred)
                    st.markdown(
                        "<p style='color: red'>Nous pouvons apercevoir que le résultat n'est pas représentatif des données rentrées</>", unsafe_allow_html=True)
            except:
                pass

    with col2:
        st.subheader('délai de livraison')

        form = st.form(key="order_estimated_delivery_date prediction_form")

        feature1 = form.number_input('feature1')
        feature2 = form.number_input('feature2')
        feature3 = form.number_input('feature3')
        feature4 = form.number_input('feature4')
        feature5 = form.number_input('feature5')
        button = form.form_submit_button("Predict")

        data = {
            'feature1': feature1,
            'feature2': feature2,
            'feature3': feature3,
            'feature4': feature4,
            'feature5': feature5,
        }

        if button:
            st.write('le délai de livraison est estimé à :')

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 50px; margin-top: 50px'>Graphiques</h1>",
            unsafe_allow_html=True)
