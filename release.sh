#!/bin/bash

python manage.py migrate
python manage.py makesuperuser
python manage.py collectstatic --noinput