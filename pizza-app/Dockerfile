# Author: Hunter Jones

# Set base image and instantiate Ubuntu (jammy)
FROM ubuntu:22.04
LABEL maintainer="Hunter Jones <joneshu2@msu.edu>"
LABEL description="Docker Image for pizza management application"

# Update and install Ubuntu and install pip
RUN apt-get update -qq && \
    apt-get install -y python3-pip vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create app directory and copy over code
RUN mkdir /app
WORKDIR /app
COPY . /app

# Upgrade pip and install python packages and requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Open port 8080 for flask app instead of default 5000 and set environment variable
EXPOSE 8080
ENV PORT=8080

# Set as Production Environment
ENV FLASK_ENV=production

# RUN Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class eventlet --threads 8 --timeout 0 app:app