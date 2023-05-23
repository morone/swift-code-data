# Base image
FROM public.ecr.aws/docker/library/python:3.9-slim-buster as dependencies

# Set HOME path
ENV HOME=/home/app

# Create app directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Install dependencies
COPY requirements.txt $HOME/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and modules
COPY app.py $HOME/
COPY swift_data_scraper.py $HOME/

# Expose port
EXPOSE 5000

# Set user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser $HOME
USER appuser

# Start the application
CMD ["python", "app.py"]
