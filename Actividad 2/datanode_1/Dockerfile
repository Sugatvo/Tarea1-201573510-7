# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /datanode_1

# Copy the current directory contents into the container at /app
COPY . /datanode_1

# Define environment variable
ENV NAME World2

# Run app.py when the container launches
CMD ["python", "datanode_1.py"]
