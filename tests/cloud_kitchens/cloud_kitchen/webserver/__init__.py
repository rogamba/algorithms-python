from flask import Flask, g, jsonify
from flask import redirect, url_for, render_template
from cloud_kitchen.cloud_kitchen import CloudKitchen
from cloud_kitchen.broker.file_broker import FileBasedBroker
from cloud_kitchen.dispatcher.driver_dispatcher import DriverDispatcher
from cloud_kitchen.shelf_client.in_memory import InMemoryShelfClient
from cloud_kitchen.order_queue.in_memory import InMemoryOrderQueue
from cloud_kitchen.shelf_manager import ShelfManager
from cloud_kitchen.waste_collector import WasteCollector
from config import *
import logging
import json
import datetime
import json
import os

LOG = logging.getLogger(__name__)
template_dir =  os.path.join(os.path.dirname(__file__), 'views')

# Shelf client
shelf_client = InMemoryShelfClient()

# Execute kitchen
kitchen = CloudKitchen(
    order_queue=InMemoryOrderQueue(),
    shelves=ShelfManager(
        shelf_client,
        SHELVES
    ),
    dispatcher=DriverDispatcher(
        shelf_client
    ),
    collector=WasteCollector(
        SHELVES,
        shelf_client,
        WASTE_COLLECTOR_FREQUENCY 
    ) 
)

# Order Broker simulator
broker = FileBasedBroker(
    filename=BROKER_FILE, 
    queue=kitchen.order_queue.orders,
    incomming_rate=INCOMMING_ORDERS_RATE
)

# Start server to fetch data
flask_app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)
flask_app.config.from_object('config')

@flask_app.route('/')
@flask_app.route('/dashboard')
def main():
    """ Check for update
    """
    return render_template('dashboard.html')

@flask_app.route('/update')
def update():
    """ Check for update
    """
    return jsonify(kitchen.get_state())

@flask_app.route('/start_simulation', methods=['POST'])
def start_simulation():
    """ Start simulation
    """
    if not hasattr(g,'_simulation'):
        broker.start_placing()
        g._simulation = True
    return jsonify({"result":"OK"})

@flask_app.route('/info')
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


flask_app.run()

