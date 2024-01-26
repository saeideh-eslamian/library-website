FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy the .env file to the container
COPY .env .

# Set environment variable for decouple to read the .env file
ENV DJANGO_READ_DOT_ENV_FILE True

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]