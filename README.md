# Prometheus Temperature exporter

Prometheus Endpoint, written in Python to read DHT11 1wire sensor and expose temperature values as a prometheus metric.

# Project structure

../
  -- Dockerfile
  -- README.md
  -- src/endpoint.py
  -- res/requirements.txt

# Prerequisites

Make sure, you have kernelmodules loaded. To do so, follow these steps: 

`sh
sudo modprobe w1-gpio
sudo modprobe w1-therm
sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt
lsmod #check if modules are loaded correctly
`


# Implementation

python shit here


# Dockerrization

I've used hypriot os with a RaspberryPi2. Works pretty fine, although Docker builds might take some time.


# Security
nginx conf and sudo apt-get install apache2-utils -y here

# Accessibility

freetz exposes


# Run it

Just run the container. Feel free to pass the container to an orchestrator. 

`docker run -it -e TEMPEXPORTER_PORT=9102 -p 9102:9102 tempexporter:1.0`

# Open ToDo's
  - Complete documentation
  - Add "suppress container logoutput" option
  - Add Makefile
  - Add CI/CD Support
  - Add Adafruit humidity sensor capability
  - Add Basic Auth to prometheus endpoint