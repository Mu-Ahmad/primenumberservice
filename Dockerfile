# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port that the Django app will be running on
EXPOSE 8000

# Start the Celery worker and beat processes when the container starts
CMD ["sh", "-c", "celery -A primeservice worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler && python manage.py runserver 0.0.0.0:8000"]
