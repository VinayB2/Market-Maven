# Contents of ~/my_app/streamlit_app.py
import streamlit as st
def Home():
    st.markdown("# Stock Price Prediction")
    st.sidebar.markdown("# Home")
def Predictions():
    st.markdown("# Predictions")
    st.sidebar.markdown("# Predictions")
def Trending():
    st.markdown("# Trending")
    st.sidebar.markdown("# Trending")
def HeatMap():
    st.markdown("# HeatMap")
    st.sidebar.markdown("# HeatMap")
def ChatBot():
    st.markdown("# ChatBot")
    st.sidebar.markdown("# ChatBot")
page_names_to_funcs = {
    "Home": Home,
    "Predictions": Predictions,
    "Trending": Trending,
    "HeatMap":HeatMap,
    "ChatBot":ChatBot,
}
# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()
st.write("# MarketMaven")
st.write("")
st.subheader(" Investing in stocks involves risks, including potential loss of principal. Perform due diligence before making any investment decisions")

for i in range (17):
    st.write("")
st.write("Made with ❤️ by Lunatic-Bytes")
st.write("MarketMaven means Accuracy")