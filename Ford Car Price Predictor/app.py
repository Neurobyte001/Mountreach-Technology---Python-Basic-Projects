#Q1. Setup and Libraries

#===============================================================

# Importing Streamlit library to create the web application
import streamlit as st

# Importing Pandas library for data manipulation
import pandas as pd

# Importing Joblib library to load saved machine learning model
import joblib

#===============================================================

#Q2. Loading Model and Preprocessing Objects

#===============================================================

# Loading the trained Linear Regression model
model = joblib.load("LR_ford_car.pkl")

# Loading the Standard Scaler
scaler = joblib.load("scaler.pkl")

# Loading encoded column names
encoded_columns = joblib.load("columns.pkl")

#===============================================================

#Q3. Page Configuration

#===============================================================

# Configuring the Streamlit page
# page_title sets the browser tab title
# layout="centered" keeps the page content nicely centered

st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)

#===============================================================

#Q4. Title and Description

#===============================================================

st.title("🚗 Ford Car Price Predictor")

st.write(
    "Enter the car details below to predict its selling price."
)

#===============================================================

#Q5. Numerical Input Fields

#===============================================================

year = st.number_input(
    "Manufacturing Year",
    min_value=1990,
    max_value=2025,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=300000,
    value=25000
)

tax = st.number_input(
    "Road Tax",
    min_value=0,
    max_value=1000,
    value=150
)

mpg = st.number_input(
    "Miles Per Gallon (MPG)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0.0,
    max_value=10.0,
    value=1.5
)

#===============================================================

#Q6. Categorical Input Fields

#===============================================================

# selectbox provides a dropdown menu which prevents invalid user input

transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual", "Semi-Auto"]
)

fuelType = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

#===============================================================

#Q7. Text Input and Predict Button

#===============================================================

model_name = st.text_input(
    "Car Model"
)

predict = st.button("Predict Price")

#===============================================================

#Q8. Create DataFrame and Encode

#===============================================================

if predict:

    # Creating DataFrame from user inputs

    input_data = pd.DataFrame({

        "model":[model_name],

        "year":[year],

        "transmission":[transmission],

        "mileage":[mileage],

        "fuelType":[fuelType],

        "tax":[tax],

        "mpg":[mpg],

        "engineSize":[engineSize]

    })

    #===========================================================

    # Performing One-Hot Encoding

    input_data = pd.get_dummies(input_data)

    #===========================================================

    # Matching columns with training data

    input_data = input_data.reindex(
        columns=encoded_columns,
        fill_value=0
    )


#Q9. Scaling and Prediction

    #===========================================================

    numerical_columns = [
        "year",
        "mileage",
        "tax",
        "mpg",
        "engineSize"
    ]

    # Applying Feature Scaling

    input_data[numerical_columns] = scaler.transform(
        input_data[numerical_columns]
    )

    #===========================================================

    # Predicting Price

    prediction = model.predict(input_data)

    #===========================================================

    st.success(
        f"Predicted Price : £{prediction[0]:,.2f}"
    )

#===============================================================