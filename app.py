import streamlit as st
import numpy as np
import pickle

# Load the trained model (assuming it's saved as a pickle file)
model = pickle.load(open('saved_model.pkl', 'rb'))

st.title('Diabetes Prediction App')

# Create input fields for the features
pregnancies = st.number_input('Pregnancies', 0, 20, 1)
glucose = st.number_input('Glucose', 0, 200, 100)
blood_pressure = st.number_input('Blood Pressure', 0, 122, 80)
skin_thickness = st.number_input('Skin Thickness', 0, 99, 20)
insulin = st.number_input('Insulin', 0, 846, 79)
bmi = st.number_input('BMI', 0.0, 70.0, 25.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', 0.0, 2.5, 0.5)
age = st.number_input('Age', 10, 100, 30)

# Create a button for prediction
if st.button('Predict'):
    # Collect the inputs into a NumPy array for model prediction
    new_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    prediction = model.predict(new_data)

    if prediction == 1:
        st.write('The patient is likely to be Diabetic.')
    else:
        st.write('The patient is not Diabetic.')
