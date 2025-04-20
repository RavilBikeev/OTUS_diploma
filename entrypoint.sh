#!/bin/sh

set -e

echo "Применяем миграции..."
python manage.py migrate --noinput

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Запускаем Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000
