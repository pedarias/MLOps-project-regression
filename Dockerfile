# Use the official TensorFlow GPU image
FROM tensorflow/tensorflow:latest-gpu

# Upgrade pip and install virtualenv
RUN pip install --upgrade pip
RUN pip install virtualenv

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Copy the models directory to the container
COPY models /app/models

# Create and activate a virtual environment
RUN virtualenv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install TensorFlow inside the virtual environment
RUN pip install --no-cache-dir --ignore-installed tensorflow

# Install required Python packages inside the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your FastAPI application runs on
EXPOSE 80

# Set the command to run your FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
