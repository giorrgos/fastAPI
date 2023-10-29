import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

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
joblib.dump(model, 'car-recommender.joblib')


