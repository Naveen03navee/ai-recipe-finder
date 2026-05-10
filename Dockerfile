# Use an official, lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements first (to leverage Docker cache)
# Wait, we haven't made a requirements.txt yet! We will do that in the next step.
COPY requirements.txt .

# Install dependencies
RUN pip install --default-timeout=100 -r requirements.txt
# Copy the rest of your application code
COPY engine.py main.py ./

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]