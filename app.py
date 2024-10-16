
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('svm_model.pkl')

# Streamlit app title
st.title('Diabetes Prediction App')

# Input fields for user data
glucose = st.number_input('Glucose Level', min_value=0)
blood_pressure = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin Level', min_value=0)
bmi = st.number_input('Body Mass Index (BMI)', min_value=0.0, format="%.2f")
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.2f")
age = st.number_input('Age', min_value=0)

# When the user clicks the predict button
if st.button('Predict'):
    new_data = np.array([[glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(new_data)

    # Display the prediction
    if prediction[0] == 1:
        st.write('Predicted Class: Diabetic')
    else:
        st.write('Predicted Class: Non-Diabetic')
