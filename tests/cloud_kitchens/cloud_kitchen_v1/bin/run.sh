#!/bin/bash

# if app dir not set, set to app name
if [[ -z $APP_DIR ]]
    then
    APP_DIR="/$APP_NAME"
fi

echo "Starting $APP_NAME in $MODE mode"
echo "Root app dir: $APP_DIR"
cd $APP_DIR
/bin/bash env/bin/activate

# Init the database
env/bin/flask initdb

# Evaluate the mode of execution and the 
then
# Run celery
echo "Starting Celery..."
env/bin/celery worker -A app.celery_tasks -c 3 -n $APP_NAME"_"$RANDOM  & 
# Run gunicorn
echo "Starting Web Service"
env/bin/gunicorn --workers 3 --bind unix:geoprice.sock -t 200 -m 000 wsgi:app &
nginx -g "daemon off;"

