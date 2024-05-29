# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Environment Variables
ENV FLASK_APP main
ENV FLASK_ENV development

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]