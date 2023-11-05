import streamlit as st
import requests

# Define the API endopoint URL
api_url = "http://127.0.0.1:8000/car/predict"

# Define a function to make the API requests
def call_api(endpoint, data):
    response = requests.post(endpoint, json=data)
    return response.json()

# Create a Streamlit app
def main():
    st.title("Car Prediction App")
    
    # Create input fields for age and gender
    age = st.number_input("Enter Age", min_value=0)
    gender = st.selectbox("Select Gender", ["Male", "Female"])

    # Map the gender selection to an integer (you can modify this as per your API)
    gender_mapping = {"Male": 0, "Female": 1}
    gender_int = gender_mapping.get(gender)

    # Create a button to trigger the API call
    if st.button("Predict"):
        data = {"age": age, "gender": gender_int}
        result = call_api(api_url, data)
        st.write("Prediction:", result)  # Display the API response

if __name__ == "__main__":
    main()

# streamlit run app.py

# docker run -p 8501:8501 car_recommender_frontend:latest