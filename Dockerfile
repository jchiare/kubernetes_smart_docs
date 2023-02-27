# Use an official Python runtime as a parent image
FROM python:3.10.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install Rust for tiktoken dependency
RUN apt-get update && apt-get install -y build-essential curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy the requirements file first and install packages
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY kubernetes_smart_docs /app/kubernetes_smart_docs

# Expose port 8000
EXPOSE 8000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the command to start the Flask server
CMD ["flask", "--app", "kubernetes_smart_docs/app", "run", "-p", "8000", "-h", "0.0.0.0"]
