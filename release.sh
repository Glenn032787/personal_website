#!/bin/bash

bash update_publication.sh
python manage.py makesuperuser
python manage.py migrate
