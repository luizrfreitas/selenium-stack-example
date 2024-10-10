FROM python:3.9-slim

# Set the working directory
# WORKDIR /app

# Copy requirements.txt (or Pipfile.lock)
COPY ../requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
# COPY . .

# Set the PYTHONPATH to include the src directory
ENV PYTHONPATH=/src

# Set the entry point for running the application
# CMD ["python", "app.py"]
