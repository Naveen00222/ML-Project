import streamlit as st
import pickle
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺", layout="centered")

# --- Futuristic Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

    body {
        font-family: 'Orbitron', sans-serif;
        background: radial-gradient(circle at 20% 30%, #0b0c10, #1f2833, #0b0c10);
        color: white;
    }

    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.pinimg.com/originals/8a/58/4c/8a584c5b93f60cb329a4c25b36cf1d36.gif");
        background-size: cover;
        background-attachment: fixed;
    }

    h1, h2, h3 {
        color: #66fcf1;
        text-align: center;
        text-shadow: 0 0 20px #ff073a;
    }

    .stButton>button {
        background: linear-gradient(90deg, #ff073a, #045de9);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 0.75em 1.5em;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 25px #045de9;
    }

    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 35px #ff073a;
    }

    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>🔮 AI-Powered Diabetes Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; color:#C5C6C7; font-size:18px;'>
Enter your details below to get your personalized <b>Diabetes Risk Score</b>  
based on clinical and lifestyle indicators.
</div><br>
""", unsafe_allow_html=True)

# --- Load Trained Model and Encoders ---
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
lab_enc_gender = pickle.load(open('label_enc_gender.pkl', 'rb'))
lab_enc_smoking = pickle.load(open('label_enc_smoking.pkl', 'rb'))

# --- User Inputs ---
age = st.number_input("Age", min_value=10, max_value=100, value=None, placeholder="Enter age")
gender = st.selectbox("Gender", ["Select...", "Male", "Female"])
smoking_status = st.selectbox("Smoking Status", ["Select...", "Current", "Former", "Never"])
alcohol = st.number_input("Alcohol Consumption (litres/week)", min_value=0.0, max_value=20.0, value=None)
activity = st.number_input("Physical Activity (minutes/week)", min_value=0.0, max_value=1000.0, value=None)
diet_score = st.slider("Diet Score (0–10)", 0.0, 10.0, 5.0)
sleep = st.slider("Sleep Hours per Day", 0.0, 24.0, 7.0)
screen_time = st.number_input("Screen Time (hours/day)", min_value=0.0, max_value=24.0, value=None)

family = st.radio("Family History of Diabetes", ["Yes", "No"], index=None)
hyper = st.radio("Hypertension History", ["Yes", "No"], index=None)
cardio = st.radio("Cardiovascular History", ["Yes", "No"], index=None)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=None)
waist_hip = st.number_input("Waist-to-Hip Ratio", min_value=0.5, max_value=2.0, value=None)
systolic = st.number_input("Systolic BP (mmHg)", min_value=80.0, max_value=200.0, value=None)
diastolic = st.number_input("Diastolic BP (mmHg)", min_value=40.0, max_value=120.0, value=None)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, max_value=150.0, value=None)
chol_total = st.number_input("Total Cholesterol (mg/dL)", min_value=100.0, max_value=400.0, value=None)
hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20.0, max_value=100.0, value=None)
ldl = st.number_input("LDL Cholesterol (mg/dL)", min_value=50.0, max_value=300.0, value=None)
triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=50.0, max_value=500.0, value=None)
glucose_fasting = st.number_input("Fasting Glucose (mg/dL)", min_value=60.0, max_value=300.0, value=None)
glucose_post = st.number_input("Postprandial Glucose (mg/dL)", min_value=90.0, max_value=400.0, value=None)
insulin = st.number_input("Insulin Level (µU/mL)", min_value=1.0, max_value=50.0, value=None)
hba1c = st.number_input("HbA1c (%)", min_value=3.0, max_value=20.0, value=None)

# --- Prediction Logic ---
if st.button("🚀 Predict My Diabetes Risk"):
    if (
        None in [age, alcohol, activity, screen_time, bmi, waist_hip, systolic, diastolic,
                 heart_rate, chol_total, hdl, ldl, triglycerides, glucose_fasting, glucose_post,
                 insulin, hba1c]
        or "Select..." in [gender, smoking_status]
        or None in [family, hyper, cardio]
    ):
        st.error("⚠️ Please fill in all required fields before predicting.")
    else:
        # Encode categorical inputs
        gender_enc = int(lab_enc_gender.transform([gender])[0])
        smoking_enc = int(lab_enc_smoking.transform([smoking_status])[0])
        family_enc = 1 if family == "Yes" else 0
        hyper_enc = 1 if hyper == "Yes" else 0
        cardio_enc = 1 if cardio == "Yes" else 0

        # Prepare data
        input_data = np.array([[age, gender_enc, smoking_enc, alcohol, activity, diet_score, sleep,
                                screen_time, family_enc, hyper_enc, cardio_enc, bmi, waist_hip,
                                systolic, diastolic, heart_rate, chol_total, hdl, ldl,
                                triglycerides, glucose_fasting, glucose_post, insulin, hba1c]])

        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)
        score = prediction[0]

        # Display result
        st.success(f"🎯 **Predicted Diabetes Risk Score: {score:.2f}**")

        if score < 10:
            st.info("🟢 Low Risk — Maintain your healthy habits!")
        elif score < 20:
            st.warning("🟡 Moderate Risk — Consider consulting a doctor.")
        else:
            st.error("🔴 High Risk — Please seek medical advice soon.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#45a29e;'>© 2025 Futuristic Health AI | Powered by Streamlit</div>", unsafe_allow_html=True)
