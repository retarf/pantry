#!/bin/bash

python /scripts/connection_test
python manage.py runserver 0.0.0.0:${BE_PORT}
