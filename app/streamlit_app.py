import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("xgb_model.pkl", "rb"))

st.title("Customer Churn Prediction App")

# Input fields
gender = st.selectbox("Gender", ["Female", "Male"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner?", ["No", "Yes"])
dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["No", "Yes"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
monthly_charges = st.slider("Monthly Charges", 0.0, 150.0, 70.0)
total_charges = st.slider("Total Charges", 0.0, 10000.0, 2500.0)

multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", 
    "Mailed check", 
    "Bank transfer (automatic)", 
    "Credit card (automatic)"
])

# Base input dictionary
input_dict = {
    "SeniorCitizen": int(senior_citizen),
    "Partner": 1 if partner == "Yes" else 0,
    "Dependents": 1 if dependents == "Yes" else 0,
    "tenure": tenure,
    "PhoneService": 1 if phone_service == "Yes" else 0,
    "PaperlessBilling": 1 if paperless_billing == "Yes" else 0,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "gender_Male": 1 if gender == "Male" else 0,
    f"MultipleLines_{multiple_lines}": 1,
    f"InternetService_{internet_service}": 1,
    f"OnlineSecurity_{online_security}": 1,
    f"OnlineBackup_{online_backup}": 1,
    f"DeviceProtection_{device_protection}": 1,
    f"TechSupport_{tech_support}": 1,
    f"StreamingTV_{streaming_tv}": 1,
    f"StreamingMovies_{streaming_movies}": 1,
    f"Contract_{contract}": 1,
    f"PaymentMethod_{payment_method}": 1
}

# Get the feature list from the model
expected_columns = model.get_booster().feature_names

# Fill missing features with 0s
input_data = {col: input_dict.get(col, 0) for col in expected_columns}
input_df = pd.DataFrame([input_data])

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    st.success("Prediction: Customer will CHURN" if prediction == 1 else "Prediction: Customer will NOT churn")
