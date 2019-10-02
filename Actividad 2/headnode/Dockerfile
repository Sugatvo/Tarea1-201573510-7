# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /headnode

# Copy the current directory contents into the container at /app
COPY . /headnode

# Define environment variable
ENV NAME World5

# Run app.py when the container launches
CMD ["python", "headnode.py"]
