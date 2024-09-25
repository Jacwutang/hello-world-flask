FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install flask

# Expose port 5000 for Flask
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]