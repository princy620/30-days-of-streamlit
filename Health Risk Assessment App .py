import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Health Risk Assessment", page_icon="🩺", layout="centered")

# Title and introduction
st.title("🩺 Health Risk Assessment App")
st.write(
    "Discover your health risk scores and gain insights for better living! "
    "Your health is your most valuable asset—let's ensure it's in great shape."
)

# Inputs
age = st.number_input("Age (years)", 0, 120, 30)
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 22.0, 0.1)
st.write("Normal BMI: 18.5 - 24.9")

blood_pressure = st.number_input("Blood Pressure (Systolic mm Hg)", 50, 200, 120)
st.write("Normal BP: Less than 120 mm Hg")

cholesterol = st.number_input("Cholesterol Level (mg/dL)", 100, 400, 180)
st.write("Desirable cholesterol: Less than 200 mg/dL")

fasting_bs = st.number_input("Fasting Blood Sugar (mg/dL)", 50, 300, 90)
st.write("Normal fasting blood sugar: 70 - 99 mg/dL")

hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.0, 0.1)
st.write("Normal HbA1c: Less than 5.7%")

smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
drinking = st.selectbox("Do you drink alcohol?", ["No", "Yes"])

screen_time = st.slider("Daily Screen Time (hours)", 0, 16, 4)
outdoor_activity = st.selectbox("Do you engage in outdoor activities?", ["Yes", "No"])

# Health Tips Section
if st.button("Assess Health and Get Tips"):
    heart_risk = 0
    diabetes_risk = 0

    # Age factor
    if age > 60:
        heart_risk += 35
        diabetes_risk += 25
    elif age > 45:
        heart_risk += 20
        diabetes_risk += 10

    # BMI factor
    if bmi >= 30:
        heart_risk += 30
        diabetes_risk += 35
    elif bmi >= 25:
        heart_risk += 15
        diabetes_risk += 20

    # Blood pressure
    if blood_pressure >= 130:
        heart_risk += 25
    elif blood_pressure >= 120:
        heart_risk += 10

    # Cholesterol
    if cholesterol >= 240:
        heart_risk += 20
    elif cholesterol >= 200:
        heart_risk += 10

    # Fasting Blood Sugar
    if fasting_bs >= 126:
        diabetes_risk += 40
    elif fasting_bs >= 100:
        diabetes_risk += 20

    # HbA1c
    if hba1c >= 6.5:
        diabetes_risk += 40
    elif hba1c >= 5.7:
        diabetes_risk += 20

    # Smoking and drinking
    if smoking == "Yes":
        heart_risk += 30
    if drinking == "Yes":
        heart_risk += 10
        diabetes_risk += 10

    # Screen time and outdoor activities
    if screen_time > 6:
        heart_risk += 10
        diabetes_risk += 10
    if outdoor_activity == "No":
        heart_risk += 10
        diabetes_risk += 10

    # Clamp risk scores between 0 and 100
    heart_risk = max(0, min(100, heart_risk))
    diabetes_risk = max(0, min(100, diabetes_risk))

    # Results
    st.success(f"🫀 Heart Disease Risk Score: {heart_risk}%")
    st.success(f"🩸 Diabetes Risk Score: {diabetes_risk}%")

    # Health Tips
    st.subheader("Health Improvement Tips:")
    st.write("“To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.” — Buddha")

    if heart_risk > 50 or diabetes_risk > 50:
        st.write("- Reduce screen time and engage in outdoor activities.")
        st.write("- Incorporate breathing exercises and yoga into your routine.")
        st.write("- Stay active with a mix of cardio and strength exercises.")
        st.write("- Limit alcohol and avoid smoking.")
        st.write("- Follow a balanced diet and monitor your blood pressure and sugar levels.")
    else:
        st.write("- Maintain your healthy lifestyle and stay consistent!")
