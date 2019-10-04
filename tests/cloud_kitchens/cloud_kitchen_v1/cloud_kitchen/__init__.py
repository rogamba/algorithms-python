from flask import Flask, request, session, g, redirect, jsonify
from flask import redirect, url_for, render_template
from config import *
#from models.kitchen import Kitchen
import logging
import json
import datetime


app = Flask(__name__)
app.config.from_object('config')

# Logger
logger = logging.getLogger(__name__)

# Build kitchen intance
#broker = Broker()
#kitchen = Kitchen(broker=Broker, order=Order)

# Database global functions
@app.before_request
def before_request():
    # Thing to do before request
    g._kitchen = kitchen
    pass


@app.route('/')
@app.route('/dashboard')
def main():
    """ Main route
    """
    error=None
    session['lang'] = lang
    return render_template()

@app.route('/update')
def update():
    """ WebSocket update info route
    """
    error=None
    session['lang'] = lang
    return jsonify({})


@app.route('/info')
def info():
    """ Main route
    """
    # Validar si el usuario ya está loggeado
    return jsonify({
        "version" : "0.1",
        "author" : "Rodrigo Gamba",
        "name" : "Cloud Kitchen",
        "description" : "Kitchen simulator for receiving, categorizing and dispatching orders."
    })


#Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "not found"
    }), 400

# HTTP Error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "bad request"
    }), 400


# Secret key
app.secret_key = app.config['SECRET_KEY']

if __name__ == '__main__':
    # Init db and so...
    app.run(host='0.0.0.0',port=80,debug=True)
