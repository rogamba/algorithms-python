# Cloud Kitchen

Kitchen simulator for receiving, categorizing and dispatching orders. The core application executes three threads to simulate the
main actions of the application: place new orders, process the orders and dispatch them. The application also runs a web server
that fetches the state of the kitchen's shelves and orders and display

## Configuration variables

#### Application Specific
* **WASTE_COLLECTOR_FREQUENCY**: Frequency in seconds that the waste collector will scan and cleanup the shelves
* **SHELVES**: List of dictionaries containing:
  - name of the shelf
  - capacity: Maximum number of orders that fit in the shelf
  - decay factor: Until now only the overflow shelf has a decay factor of 2

#### Broker Simulator
* **INCOMMING_ORDERS_RATE**: To calculate the Poisson s
* **BROKER_FILE** = Filename that contains the example orders list, located inside `/data' directory

### Pre-requirements

- Flask>=0.12.2

## Building Docker Image
To build the docker image execute:
```shell
$> docker build -t cloud_kitchen --no-cache . 
```
Once built, to run the container execute:
```shell
$> docker run -d -p <local_port>:80 --name <app_name> cloud_kitchen:latest
```

You can check if the application is running by visiting the ip of you docker dhost on the mapped port that you specified.

## Starting simulation

To start running the simulation you have to click on the "Start processing orders" in the main screen of the application, this will trigger the broker thread which will start sending orders at a rate of 3.25 orders per second on average. The state of every shelf will appear on the screen with its respective list of orders. 

## Running tests
There is a bash file to execute all tests located at `/bin/tests.sh`, you can execute it through:
```shell
$> /bin/bash bin/test.sh
```
Or you can execute the tests manually with:
```shell
$> python -m test.test_file_broker &&
python -m test.test_inmemory_shelf &&
python -m test.test_shelf_manager &&
python -m test.test_driver_dispatcher &&
python -m test.test_kitchen
```

## Contracts

### Fetch state

Get kitchen state data, it returns an object of every shelf with a list of their current orders

**Method**:  GET

**Endpoint**: `/update/`

**Response:**

```json
{
    "hot" : [
        {
            "decay_rate": 0.2,
            "id": "6dd7d5fa-364b-46ba-a890-6363a7b30082",
            "name": "Cheese",
            "normalized_value": 0.9688032015632181,
            "shelf_life": 255,
            "temp": "cold",
            "value": 247.04481811523436
        }
    ],
    "overflow" : [
        {
            "decay_rate": 0.7,
            "id": "d1f81365-292f-4eeb-898a-5dbd36559cda",
            "name": "Pork Chop",
            "normalized_value": 0.9511054315567017,
            "shelf_life": 200,
            "temp": "hot",
            "value": 190.22108914852143
        }
    ]  
}
```
