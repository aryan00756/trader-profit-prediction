import streamlit as st
import pandas as pd
import joblib
from tensorflow import keras


model = keras.models.load_model("trader_model.keras")
scaler = joblib.load("scaler.pkl")

st.title("Trader Profitability Predictor")

trade_count = st.number_input("Trades per day", min_value=0, value=10)
avg_trade_size = st.slider("Average trade size (USD)", min_value=0, max_value=50000, value=500, step=100)
sentiment = st.selectbox("Market sentiment", ["Fear", "Greed"])

sentiment_value = 0 if sentiment == "Fear" else 1

if st.button("Predict"):

    input_df = pd.DataFrame(
        [[trade_count, avg_trade_size, sentiment_value]],
        columns=['trade_count','avg_trade_size','sentiment']
    )

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0][0]

    st.write("Profit Probability:", round(float(prediction), 2))

    if prediction > 0.5:
        st.success("Model predicts PROFITABLE day.")
    else:
        st.error("Model predicts LOSS day.")