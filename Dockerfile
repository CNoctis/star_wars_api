FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Update the system and prepare the environment for installation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest safe version (23.3 or higher)
RUN python -m pip install --upgrade pip

# Upgrade setuptools to the latest safe version (>= 70.0.0)
RUN python -m pip install --upgrade setuptools

# Copy the application's requirements file into the container
COPY requirements.txt ./

# Install the application's dependencies without using cache
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Gunicorn como servidor WSGI
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the application files
COPY . .

# Command to start the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
