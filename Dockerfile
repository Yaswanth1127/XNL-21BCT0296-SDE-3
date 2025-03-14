# Base Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose necessary ports
EXPOSE 5000

# Command to run the application
CMD ["python", "src/transaction_processor.py"]
