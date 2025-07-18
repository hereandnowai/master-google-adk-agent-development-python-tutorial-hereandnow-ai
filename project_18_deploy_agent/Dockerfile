
# Use the official Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application file.
COPY main.py .

# Expose the port the app runs on.
EXPOSE 8080

# Run the application.
CMD ["python", "main.py"]
