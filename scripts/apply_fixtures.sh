#!/bin/bash

./manage.py loaddata event_fixtures
./manage.py loaddata user_fixtures
./manage.py loaddata guest_fixtures
