# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /servidor

# Copy the current directory contents into the container at /app
COPY . /servidor

# Define environment variable
ENV NAME World1

# Run app.py when the container launches
CMD ["python", "servidor.py"]
