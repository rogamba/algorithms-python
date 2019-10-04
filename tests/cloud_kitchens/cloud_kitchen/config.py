# -*- coding: utf-8 -*-
import os
import sys

APP_NAME = os.getenv('APP_NAME','cloud_kitchen')
APP_SECRET = "joiu??oasAIasda9&#934)(ASSD?__asd0"
SECRET_KEY = APP_SECRET
TESTING=False

# App directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR=BASE_DIR
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

# Behaviour config variables
INCOMMING_ORDERS_RATE = 3.25
BROKER_FILE = 'orders.json'
WASTE_COLLECTOR_FREQUENCY = 1
SHELVES = [
    {
        "name" : "hot",
        "capacity" : 15,
        "decay_factor" : 1
    },
    {
        "name" : "cold",
        "capacity" : 15,
        "decay_factor" : 1
    },
    {
        "name" : "frozen",
        "capacity" : 15,
        "decay_factor" : 1
    },
    {
        "name" : "overflow",
        "capacity" : 20,
        "decay_factor" : 2
    }
]

# Env-dependent variables
ENV = os.getenv('ENV','DEV')