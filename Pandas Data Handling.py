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
df_encoded = pd.get_dummies(df,columns=['Brand'])


#Data Assigning

X = df_encoded.drop('Selling_Price',axis=1)

y=df_encoded['Selling_Price']


# Our Model  Twin

model = LinearRegression()
model.fit(X, y)

#Pridiction and error calculation part Twin



#Serialization

joblib.dump(model, 'phone_model.pkl')

 #To dump the new brand columns
 
joblib.dump(X.columns.tolist(),'model_columns.pkl')



print("Successfully model trained with the Age , Original price , Battery , RAM , storage, Condition score , and Brand !!!")