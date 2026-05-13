# Here We Use Streamlit !!!! Twin for web app

import streamlit as st

# a small css injection to remove the logo of streamlit twin


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



import pandas as pd
import joblib

# Load the model and the column names we saved as .pkl Twin!!


model = joblib.load('phone_model.pkl')
model_columns = joblib.load('model_columns.pkl')

#title 

st.title("AI Price Predictor")


# Extract brand names from the columns (removing the 'Brand_' prefix) to make it clear for users  twinn!


brands = [col.replace('Brand_', '') for col in model_columns if 'Brand_' in col]
selected_brand = st.selectbox("Select Brand", brands)

#input slider and price input part twin

age = st.slider("Phone Age (Years)", 0, 7, 1)
price = st.number_input("Original Price", value=10000)

# The block of code inside it works only if we click thiz buttonn twinnn !
if st.button("Calculate Prediction"):
    
   
    # Create an empty row with all columns set to 0 to make it change when user give the brand input twin
    
    
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Set the values for our inputs twin
    
    
    input_df['Age'] = age
    input_df['Original_Price'] = price
    
    # Turn on the '1' for the selected brand by the usersss
    
    
    brand_col = f"Brand_{selected_brand}"
    if brand_col in input_df.columns:
        input_df[brand_col] = 1

    # Predict
    
    
    prediction = model.predict(input_df)[0]
    
    st.success(f"Predicted Price: ₹{max(0, prediction):,.2f}")
    
