#!/usr/bin/env sh

case $1 in
    runprod )
        python manage.py collectstatic --no-input
        uvicorn noagreements.asgi:application --host 127.0.0.1 --port 8000 --env-file prod-variables.env
        ;;
    rundev)
        python manage.py runserver 0.0.0.0:8000
        ;;
    
esac
