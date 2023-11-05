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
EXPOSE 8000:8000

# Command to start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# docker build -t car_rec_backend:latest .
# docker run -p 8000:8000 car_rec_backend:latest