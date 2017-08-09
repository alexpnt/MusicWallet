#!/bin/sh

python manage.py makemigrations --settings=musicwalletproject.settings.development
python manage.py migrate --settings=musicwalletproject.settings.development
python manage.py collectstatic --settings=musicwalletproject.settings.development --noinput
python manage.py runserver 0.0.0.0:8000 --settings=musicwalletproject.settings.development

