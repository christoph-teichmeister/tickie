#!/bin/bash

echo Applying database migrations
python manage.py migrate
echo Database migrations done.

echo "Starting django server (runserver) on 0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000
