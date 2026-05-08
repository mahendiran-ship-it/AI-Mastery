#  This are the Libraries Twin


# Pandas used to handle data and csv files

import pandas as pd

#Here we use Joblib to save our brain("Serialization")

import joblib

#This is Scikit-Learn , A ML library that haz many models in it 

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error



#CSV file Loading part , Twin

df = pd.read_csv('marketplace_data.csv')



#Automatic Empty data filling part

df['selling_price'] = df['selling_price'].fillna(df['selling_price'].mean())

#Data Assigning

X = df[['age_years', 'original_price']] 
y = df['selling_price']


# Our Model Brain Twin
brain = LinearRegression()
brain.fit(X, y)

#Pridiction and error calculation part Twin

y_pred = brain.predict(X)
error = mean_absolute_error(y, y_pred)

#Serialization

joblib.dump(brain, 'phone_model.pkl')



print(f"Training Complete. Avg Error: ₹{error:.2f}")
print("Brain saved to 'phone_model.pkl'")
