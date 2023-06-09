# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]