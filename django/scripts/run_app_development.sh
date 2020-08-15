#!/usr/bin/env bash

source $(dirname "$0")/prepare_environment.sh

# Prepares directory for logs
prepare_dir;
python app/manage.py collectstatic  --no-input
python app/manage.py makemigrations --no-input
python app/manage.py migrate --no-input
python app/manage.py runserver 0.0.0.0:8000
