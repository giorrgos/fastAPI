import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle

# Load the data
cars_data = pd.read_csv('data/cars.csv')

# Split the data
X = cars_data.drop(columns=['vehicle_type']).values # Input Data
y = cars_data['vehicle_type'] # Output Dat

# Create a DecisionTreeClassfier model
model = DecisionTreeClassifier()

# Fit the model
model.fit(X, y)

# Make predictions
predictions = model.predict([ [22,1] ])
predictions[0]

# Save / Persist model
pickle.dump(model, open('car_recommender.pkl','wb'))

model = pickle.load(open('car_recommender.pkl','rb'))
model.predict([[25, 1]])


