# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /datanode_3

# Copy the current directory contents into the container at /app
COPY . /datanode_3

# Define environment variable
ENV NAME World4

# Run app.py when the container launches
CMD ["python", "datanode_3.py"]
