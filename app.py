#we use streamlit to build tge interface twin

import streamlit as st
import joblib  
import sklearn 

st.title("Local Marketplace Price Predictor")
st.write("Created By Mahendiran")

age = st.slider("Phone Age (Years)", 0, 7, 1)
price = st.number_input("Original Price", value=10000)

if st.button("Calculate Prediction"):
    model = joblib.load('phone_model.pkl')
    
    
        
    raw_prediction = model.predict([[age, price]])[0]
    final_price = max(0, raw_prediction)
    
    st.success(f"Predicted Selling Price: ₹{final_price:,.2f}")
    
         
    st.success(f"Predicted Selling Price: ₹{prediction[0]:,.2f}")
    st.balloons() 
