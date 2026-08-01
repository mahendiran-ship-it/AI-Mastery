import streamlit as st
import pandas as pd
import joblib

# 1. Axios Branding & Neon UI Styling for better User Experience Twinnn
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_page_config(page_title="Axios AI", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1 { color: #00ffcc; text-align: center; font-family: 'Courier New', monospace; letter-spacing: 2px; }
    .stSubheader { color: #ffffff; border-bottom: 1px solid #00ffcc; }
    .stSlider > div [data-baseweb="slider"] { background-color: #00ffcc; }
    div.stButton > button {
        background-color: #00ffcc;
        color: black;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        box-shadow: 0px 0px 15px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Load the Axios Brain from our phone_model.pkl twin !
model = joblib.load('phone_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("AXIOS AI")
st.write("<p style='text-align: center; color: #888;'>Pro Valuation Engine by Mahendiran</p>", unsafe_allow_html=True)

st.subheader("Device Hardware")
brands = [col.replace('Brand_', '') for col in model_columns if 'Brand_' in col]
selected_brand = st.selectbox("Market Brand", brands)

col1, col2 = st.columns(2)
with col1:
    ram = st.selectbox("RAM Capacity", [4, 6, 8, 12, 16])
with col2:
    storage = st.selectbox("Storage Capacity", [64, 128, 256, 512, 1024])

original_price = st.number_input("Original Retail Price (₹)", value=50000)

st.subheader("Usage History")
age = st.slider("Total Usage Time (Years)", 0, 7, 1)
battery = st.slider("Current Battery Health (%)", 70, 100, 95)
condition = st.select_slider("Physical Quality Score", options=[1,2,3,4,5,6,7,8,9,10], value=8)

st.write("---")

# 4. Axios Logic
if st.button("RUN AXIOS VALUATION"):
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    input_df['Age'] = age
    input_df['Original_Price'] = original_price
    input_df['Battery_Health'] = battery
    input_df['RAM'] = ram
    input_df['Storage'] = storage
    input_df['Condition_Score'] = condition
    
    brand_col = f"Brand_{selected_brand}"
    if brand_col in input_df.columns:
        input_df[brand_col] = 1

    # Raw Prediction
    prediction = model.predict(input_df)[0]
    
    # Apply Axios Premium logic for high-end brands
    if selected_brand == 'Apple': prediction *= 1.25 # iOS Value retention
    elif selected_brand == 'Samsung': prediction *= 1.1 # Flagship retention
    
    # Secure Guardrail
    final_price = min(float(original_price), max(0.0, float(prediction)))
    
    # Success Card
    st.markdown(f"""
        <div style="background-color: #1a1c24; padding: 20px; border-radius: 10px; border-left: 5px solid #00ffcc;">
            <h2 style="color: #ffffff; margin: 0;">₹{final_price:,.2f}</h2>
            <p style="color: #00ffcc; margin: 0;">Official Axios Valuation Result</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Trend Analysis
    st.write("###  Depreciation Trend")
    trend_data = []
    for y in range(8):
        temp_df = input_df.copy()
        temp_df['Age'] = y
        p = model.predict(temp_df)[0]
        if selected_brand == 'Apple': p *= 1.25
        trend_data.append(min(float(original_price), max(0.0, float(p))))
    
    st.line_chart(pd.DataFrame(trend_data, columns=["Axios Forecast"]))
    


