#we use streamlit to build tge interface twin

import streamlit as st
import joblib  <-- Add a 
import sklearn <-- Add a 

st.title("Local Marketplace Price Predictor")


age = st.slider("Phone Age (Years)", 0, 5, 1)
price = st.number_input("Original Price", value=10000)

if st.button("Calculate Prediction"):
    model = joblib.load('phone_model.pkl') <-- Add a 
    prediction = model.predict([[age, price]]) <-- Add a 
    
    
         
    st.success(f"Predicted Selling Price: ₹{prediction:,.2f}")
    st.balloons() 
