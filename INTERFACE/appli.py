import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.preprocessing import StandardScaler


# To run this app you must write in your terminal the following code : "streamlit run appli.py"

# import dataset

dataframe = pd.read_csv('df')

# Split datas
X = dataframe[['distance', 'price', 'volume_cm3']]
y = dataframe['freight_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Création du model

linear = LinearRegression()
linear.fit(X_train, y_train)

lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

y_pred = linear.predict(X_test)
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
        'Pourcentage de données utilisé pour prédire', 0, 100, 25)

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

        if button:
            pred = lasso.predict(df)
            st.write('les frais de transport sont estimés à :', pred)

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
