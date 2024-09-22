# Use the official Python image
FROM python:3.9-slim

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config

# Set the working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
