import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# Load model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter all transaction details below.")

columns = [
'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9',
'V10','V11','V12','V13','V14','V15','V16','V17',
'V18','V19','V20','V21','V22','V23','V24','V25',
'V26','V27','V28','Amount'
]

inputs = []

col1, col2, col3 = st.columns(3)

for i, feature in enumerate(columns):

    with [col1, col2, col3][i % 3]:
        value = st.number_input(
            feature,
            value=0.0,
            format="%.6f"
        )

    inputs.append(value)

if st.button("Predict"):

    data = pd.DataFrame([inputs], columns=columns)

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0]

    st.subheader("Prediction Result")

    if prediction == 0:
        st.success("✅ Legitimate Transaction")
    else:
        st.error("🚨 Fraudulent Transaction")

    st.write(f"**Legitimate Probability:** {probability[0]*100:.2f}%")
    st.write(f"**Fraud Probability:** {probability[1]*100:.2f}%")

    st.progress(int(probability[1]*100))