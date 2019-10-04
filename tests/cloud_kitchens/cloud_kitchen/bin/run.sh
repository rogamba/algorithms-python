#!/bin/bash

# if app dir not set, set to app name
if [[ -z $APP_DIR ]]
    then
    APP_DIR="/$APP_NAME"
fi

cd $APP_DIR
/bin/bash env/bin/activate
nginx -g "daemon off;" &
python -m webserver


