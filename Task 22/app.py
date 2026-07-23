# SESSION 22 - STREAMLIT APPLICATION

## Q9 & Q10. Heart Disease Prediction Web App


import streamlit as st
import pandas as pd
import joblib

#===============================================================

# Loading saved model and preprocessing objects

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

#===============================================================

# Page configuration

st.set_page_config(
    page_title="Heart Disease Predictor",
    layout="centered"
)

#===============================================================

# Title and description

st.title("❤️ Heart Disease Predictor")

st.write("Enter patient details below to predict heart disease.")

#===============================================================

# Input fields

age = st.number_input("Age", 1, 100, 55)

sex = st.selectbox("Sex", ["M", "F"])

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input("Resting Blood Pressure", 50, 250, 120)

cholesterol = st.number_input("Cholesterol", 0, 600, 200)

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.number_input("Maximum Heart Rate", 50, 250, 150)

exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])

oldpeak = st.number_input("Oldpeak", -5.0, 10.0, 1.0)

st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

#===============================================================

# Predict button

if st.button("Predict"):

    try:

        # Creating input DataFrame

        input_df = pd.DataFrame({
            "Age": [age],
            "Sex": [sex],
            "ChestPainType": [chest_pain],
            "RestingBP": [resting_bp],
            "Cholesterol": [cholesterol],
            "FastingBS": [fasting_bs],
            "RestingECG": [resting_ecg],
            "MaxHR": [max_hr],
            "ExerciseAngina": [exercise_angina],
            "Oldpeak": [oldpeak],
            "ST_Slope": [st_slope]
        })

        #=======================================================

        # Encoding categorical columns

        input_df = pd.get_dummies(input_df)

        #=======================================================

        # Aligning columns

        input_df = input_df.reindex(
            columns=columns,
            fill_value=0
        )

        #=======================================================

        # Scaling features

        input_scaled = scaler.transform(input_df)

        #=======================================================

        # Making prediction

        result = model.predict(input_scaled)[0]

        #=======================================================

        if result == 1:
            st.error("⚠️ Heart Disease: YES")
        else:
            st.success("✅ Heart Disease: NO")

    except Exception as e:
        st.error(f"Error: {e}")
        