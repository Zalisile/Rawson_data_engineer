# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install mysql-connector-python

# Copy the Python script to the working directory
COPY app.py ./

# Convert line endings to Unix format
RUN apt-get update && apt-get install dos2unix -y && dos2unix app.py

# Set the command to run your Python script
CMD ["python", "app.py"]