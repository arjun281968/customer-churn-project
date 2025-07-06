# 📉 Customer Churn Prediction App

An end-to-end machine learning web application built to predict customer churn using a telecom dataset. This project uses **XGBoost** for modeling and **Streamlit** for interactive front-end deployment.

---

## 🚀 Project Overview

Many telecom companies face high churn rates. This app helps predict which customers are likely to leave, enabling proactive retention strategies. The model is trained on customer data and served via an easy-to-use Streamlit web interface.

---

## 🧠 Features

- Data cleaning and feature engineering in Jupyter Notebook
- Model training using XGBoost with hyperparameter tuning
- Streamlit UI for real-time churn predictions
- Encoded categorical variables to match model expectations

---

## 📂 Project Structure

customer-churn-project/
├── app/
│ ├── streamlit_app.py # Streamlit web app
│ └── xgb_model.pkl # Trained XGBoost model
├── data/
│ └── customer_churn.csv # Original dataset
├── notebooks/
│ └── churn_analysis.ipynb # Data analysis + model training
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🛠️ Tech Stack

- Python
- pandas, numpy
- scikit-learn, xgboost
- Streamlit
- matplotlib, seaborn

---

## ✅ How to Run the App Locally

2.Install the required libraries:
**
pip install -r requirements.txt**

3.Run the Streamlit app:
**
cd app
streamlit run streamlit_app.py **

🌐 Live Demo
Coming soon on Streamlit Cloud()