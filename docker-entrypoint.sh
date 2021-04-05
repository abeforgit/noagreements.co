#!/usr/bin/env sh

case $1 in
    runprod )
        python manage.py collectstatic --no-input
        uvicorn noagreements.asgi:application --port 8000
        ;;
    rundev)
        python manage.py runserver 0.0.0.0:8000
        ;;
    
esac
