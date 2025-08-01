#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn hr_platform.wsgi:application --bind 0.0.0.0:8000
