#!/usr/bin/env sh

python manage.py collectstatic --no-input
uvicorn noagreements.asgi:application --port 8000
