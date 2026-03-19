# Use a small official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file first for better build cache usage
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the image
COPY . .

# Document the application port
EXPOSE 5000

# Default runtime command
CMD ["python", "app.py"]