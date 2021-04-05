#!/usr/bin/env sh

python manage.py collectstatic --no-input
uvicorn noagreements.asgi:application --host 0.0.0.0 --port 8000
