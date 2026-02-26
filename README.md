# 📈 Trader Profitability Predictor

A beginner-friendly Machine Learning web application built using TensorFlow and Streamlit that predicts whether a trader will have a profitable day based on trading behavior and market sentiment.

---

## 🚀 Project Overview

This project uses a trained Neural Network model to predict the probability of a trader being profitable.

The prediction is based on:
- Number of trades per day
- Average trade size (USD)
- Market sentiment (Fear or Greed)

The model outputs:
- A probability score (0 to 1)
- A classification: PROFITABLE or LOSS

---

## 🧠 How It Works

1. User enters trading details in the Streamlit web app.
2. Input data is scaled using a saved scaler (scaler.pkl).
3. The trained Keras model (trader_model.keras) makes a prediction.
4. The result is displayed with a probability score and decision.

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Scikit-learn
- Streamlit
- Pandas
- Joblib

---

## 📂 Project Structure

Trader-Profitability-Predictor/
│
├── app.py
├── model.ipynb
├── trader_model.keras
├── scaler.pkl
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/Trader-Profitability-Predictor.git  
cd Trader-Profitability-Predictor  

2. Create virtual environment

python -m venv venv  

Activate it:

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

3. Install dependencies

pip install -r requirements.txt  

4. Run the application

streamlit run app.py  

---

## 📊 Example Usage

Input:
- Trades per day: 15
- Average trade size: 1000
- Market sentiment: Greed

Output:
- Profit Probability: 0.72
- Model predicts PROFITABLE day

---

## 🎯 Learning Objectives

- Training a Neural Network model
- Saving and loading ML models
- Feature scaling
- Building ML-powered web apps using Streamlit
- Basic model deployment workflow

---

## 🔮 Future Improvements

- Add more trading features
- Improve model accuracy
- Deploy on Streamlit Cloud
- Add performance metrics (accuracy, confusion matrix)
- Add visual analytics dashboard

---

## 👨‍💻 Author

Aryan Yadav  
Aspiring Machine Learning Engineer
