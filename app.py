#we use streamlit to build tge interface twin

import streamlit as st
import joblib  
import sklearn 

st.title("Local Marketplace Price Predictor")


age = st.slider("Phone Age (Years)", 0, 5, 1)
price = st.number_input("Original Price", value=10000)

if st.button("Calculate Prediction"):
    model = joblib.load('phone_model.pkl')
    prediction = model.predict([[age, price]])
    
    
         
    st.success(f"Predicted Selling Price: ₹{prediction:,.2f}")
    st.balloons() 