import uvicorn
from fastapi import FastAPI
import pickle
from model_validation import CarUser

app = FastAPI()
pickle_path = open("car_recommender.pkl", "rb")
model = pickle.load(pickle_path)

# Define the routes
@app.get('/')
def index():
    return {"message: 'Cars Recommemder ML API'"}

@app.post('/car/predict')
def predict_car_type(data:CarUser):
    data = data.dict()
    age = data['age']
    gender = data['gender']

    prediction = model.predict([[age, gender]])

    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)

# uvicorn fast_api:app