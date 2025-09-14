import streamlit as st
import joblib
import numpy as np
# Load your trained model
model = joblib.load("model.pkl")  # Make sure model.pkl is in the same folder

st.title("🚀 Biofuel Energy Genreation Prediction App")
st.write("Enter the details below to predict CO2 emission:")

# Example input fields (replace with your actual dataset features)
Dairy = st.number_input(" Dairy", min_value=0.0, step=0.1)

# Convert to numpy array
input_data = np.array([[Dairy]])

if st.button("Predict Energy Generation"):
    prediction = model.predict(input_data)
    st.success(f"🌍 Estimated Biofuel Energy Genration: {prediction[0]:.2f} cu-ft")
