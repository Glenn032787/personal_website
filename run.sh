#!/bin/bash

set -e 

gunicorn mysite.wsgi --log-file - 