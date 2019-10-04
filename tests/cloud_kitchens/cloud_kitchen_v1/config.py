# -*- coding: utf-8 -*-
import os
import sys

APP_NAME = os.getenv('APP_NAME','cloud_kitchen')
APP_SECRET = "joiu??oasAIasda9&#934)(ASSD?__asd0"
SECRET_KEY = APP_SECRET
TESTING=False

# Logging and remote logging
LOG_LEVEL = os.getenv('LOG_LEVEL','DEBUG')
LOG_HOST = os.getenv('LOG_HOST', 'localhost')
LOG_PORT = os.getenv('LOG_PORT', 9090)

# App directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR=BASE_DIR
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

# Behaviour environment variables
INCOMMING_ORDERS_RATE = 3.25

# Env-dependent variables
ENV = os.getenv('ENV','DEV')