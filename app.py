import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Streamlit App
st.title('Soil Classifier')

# User Input
N = st.number_input('Nitrogen content (N)', min_value=0, max_value=300, value=0)
P = st.number_input('Phosphorous content (P)', min_value=0, max_value=300, value=0)
K = st.number_input('Potassium content (K)', min_value=0, max_value=300, value=0)
temperature = st.number_input('Temperature (°C)', min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input('pH level', min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=500.0, value=100.0)

# Convert inputs into a DataFrame
input_data = pd.DataFrame({
    'N': [N],
    'P': [P],
    'K': [K],
    'temperature': [temperature],
    'humidity': [humidity],
    'ph': [ph],
    'rainfall': [rainfall]
})

# Make a prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Recommended crop to plant in this soil is : {prediction[0]}')