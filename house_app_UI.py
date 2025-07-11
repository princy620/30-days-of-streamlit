import streamlit as st
import numpy as np
import joblib

# Load your model (Update path as needed)
model = joblib.load('lr.joblib')  # <-- Replace with correct file if needed

# Set page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Light background style
st.markdown("""
    <style>
    body, .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #2c3e50;
        font-weight: 600;
    }
    .stNumberInput label {
        font-weight: 500;python
        font-size: 15px;
        color: #34495e;
    }
    .stNumberInput input {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #ccc;
        border-radius: 6px;
        padding: 6px;
    }
    .stButton > button {
        background-color: #2980b9;
        color: white;
        padding: 0.6rem 2rem;
        font-size: 16px;
        font-weight: 600;
        border-radius: 6px;
        border: none;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #1f6391;
        transition: 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# App Title and Subtitle
st.title("🏡 House Price Prediction App")
st.markdown("Enter the following features to predict the house price using a trained Linear Regression model.")

# Input Fields in Form
with st.form("predict_form"):
    col1, col2 = st.columns(2)

    with col1:
        MedInc = st.number_input('Median Income (in 10k USD)', format="%.2f")
        HouseAge = st.number_input('House Age (in years)', format="%.2f")
        Population = st.number_input('Population', format="%.0f")

    with col2:
        AveRooms = st.number_input('Average Rooms', format="%.2f")
        AveOccup = st.number_input('Average Occupancy', format="%.2f")
        Longitude = st.number_input('Longitude', format="%.4f")

    submit = st.form_submit_button("Predict")

# Prediction Logic
if submit:
    input_data = np.array([[MedInc, HouseAge, Population, AveRooms, AveOccup, Longitude]])
    try:
        result = model.predict(input_data)[0]
        st.success(f"🏠 **Estimated House Price:** ${result:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
