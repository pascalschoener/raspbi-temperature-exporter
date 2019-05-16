#!/usr/bin/env python
"""
Prometheus running in kubernetes will automatically scrape this service.
"""
import os
import logging
from prometheus_client import start_http_server, Gauge
from w1thermsensor import W1ThermSensor

# Create a metric to track time spent and requests made.
G = Gauge('temperature_in_celcius', 'Temperature in celcuis')
SENSOR = W1ThermSensor()
LOGFORMAT = "%(asctime)s - %(levelname)s [%(name)s] %(threadName)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOGFORMAT)

def process_temperature():
    """ a function to process the temperature """
    logging.info("temperature_in_celcius: %s", SENSOR.get_temperature())
    G.set(SENSOR.get_temperature())

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    if 'EXPORTER_PORT' in os.environ:
        logging.info("Running exporter on port: %s", os.getenv('EXPORTER_PORT'))
        start_http_server(int(os.getenv('EXPORTER_PORT')))
        # call process temperature function
        while True:
            process_temperature()
    else:
        logging.error("EXPORTER_PORT variable is not set.")
