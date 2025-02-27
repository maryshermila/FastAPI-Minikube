# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x docker-entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["./docker-entrypoint.sh"]
