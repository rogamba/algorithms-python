#!/bin/bash

/bin/bash env/bin/activate
python -m test.test_file_broker &&
python -m test.test_inmemory_shelf &&
python -m test.test_shelf_manager &&
python -m test.test_driver_dispatcher &&
python -m test.test_kitchen