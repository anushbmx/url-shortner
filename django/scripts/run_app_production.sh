#!/usr/bin/env bash

source $(dirname "$0")/prepare_environment.sh

# Prepares directory for logs
prepare_dir;

echo Starting Gunicorn
exec gunicorn app.wsgi:application \
    --name app \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --chdir ./app \
    "$@"
