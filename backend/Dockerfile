# Use a secure and updated base image
FROM python:3.11.9-slim-bookworm

# Set working directory
WORKDIR /app

# Upgrade pip, install uv, and install dependencies
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app ./app

# Run the application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
