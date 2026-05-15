import streamlit as st
import pandas as pd
import joblib

# 1. Custom CSS Twin - keep it clean!
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Load the Super-Brain
model = joblib.load('phone_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title(" AI Price Predictor")
st.write("Created By Mahendiran")

# 3. Sidebar for Inputs
st.sidebar.header("Phone Specifications")

brands = [col.replace('Brand_', '') for col in model_columns if 'Brand_' in col]
selected_brand = st.sidebar.selectbox("Brand", brands)

age = st.sidebar.slider("Age (Years)", 0, 7, 1)
battery = st.sidebar.slider("Battery Health (%)", 70, 100, 95)
condition = st.sidebar.slider("Condition (1=Poor, 10=Mint)", 1, 10, 8)

ram = st.sidebar.selectbox("RAM (GB)", [4, 6, 8, 12, 16])
storage = st.sidebar.selectbox("Storage (GB)", [64, 128, 256, 512])

original_price = st.number_input("Original Price (₹)", value=25000)

# 4. Prediction Logic
if st.button("Calculate Value"):
    # Create the input row
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fill in the numerical Twin columns
    input_df['Age'] = age
    input_df['Original_Price'] = original_price
    input_df['Battery_Health'] = battery
    input_df['RAM'] = ram
    input_df['Storage'] = storage
    input_df['Condition_Score'] = condition
    
    # Set the Brand
    brand_col = f"Brand_{selected_brand}"
    if brand_col in input_df.columns:
        input_df[brand_col] = 1

    # Predict with Guardrails
    raw_prediction = model.predict(input_df)[0]
    final_price = min(float(original_price), max(0.0, float(raw_prediction)))
    
    st.success(f"### Estimated Selling Price: ₹{final_price:,.2f}")
    
    # 5. Price Trend Graph
    st.write("---")
    st.subheader(f"Depreciation Trend: {selected_brand}")
    
    trend_data = []
    for year in range(8):
        temp_df = input_df.copy()
        temp_df['Age'] = year
        p = model.predict(temp_df)[0]
        trend_data.append(min(float(original_price), max(0.0, float(p))))
    
    st.line_chart(pd.DataFrame(trend_data, columns=["Value Over Time"]))
