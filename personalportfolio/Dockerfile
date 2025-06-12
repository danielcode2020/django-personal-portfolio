# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm 

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (optional, but good practice for some libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    # Add any other system dependencies your app might need
    && rm -rf /var/lib/apt/lists/*

# Install pip and setuptools
RUN pip install --upgrade pip setuptools

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that Django will run on
EXPOSE 8000

# Run collectstatic (important for production, good for dev too)
# This command should be run in a production environment to collect all static files.
# For simplicity in development, you might skip it or run it manually if not using WhiteNoise.
# CMD ["python", "manage.py", "collectstatic", "--noinput"]

# Define the command to run your Django application
# Use 0.0.0.0 to make the server accessible from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]