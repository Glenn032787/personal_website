#!/bin/bash

python manage.py makesuperuser
python manage.py update_publications
python manage.py migrate
