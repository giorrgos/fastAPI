# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt requirements.txt

# Install all that is in the requirements.txt file
RUN pip3 install -r requirements.txt

# Copy everything from our current directory to the working area
COPY . .

# Expose the port that the FastAPI server will run on
EXPOSE 8501

# Command to start the FastAPI server
CMD ["streamlit", "run", "app.py"]

# docker build -t car_rec_frontend:latest .
# docker run -p 8501:8501 car_rec_frontend:latest