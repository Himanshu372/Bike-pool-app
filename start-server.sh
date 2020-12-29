#!/usr/bin/env bash

(cd Bike-pool-app; gunicorn Bike_Pool_App.wsgi --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"