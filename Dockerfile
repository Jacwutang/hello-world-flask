FROM python:3.10-slim

# Set working directory
WORKDIR /hello-world-flask

# Copy current directory contents into the container at /hello-world-flask
COPY . /hello-world-flask

# Install Flask
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5001

# Run the Flask app
CMD ["python", "-m", "app.run"]