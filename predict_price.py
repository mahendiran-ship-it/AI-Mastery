import joblib

#Brain Loading Part Twin

brain = joblib.load('phone_model.pkl')

print("------- AI Price Estimator -------")

#Simple User Input Twin

age = int(input("Age of phone (years): "))
price = int(input("Original price (₹): "))


#Prediction part
prediction = brain.predict([[age, price]])[0]

#Prediction if mobile is too older than my grandma

if prediction < 0:
    prediction = 0



print(f"\nSuggested Selling Price: ₹{prediction:.2f}")
