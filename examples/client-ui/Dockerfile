# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker caching
COPY requirements.txt .

# Install the required Python packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . /app

# Expose the port on which your Flask app will be listening (change to the appropriate port)
EXPOSE 7000

# Set the entrypoint to run the Flask app
ENTRYPOINT ["python", "app.py"]
