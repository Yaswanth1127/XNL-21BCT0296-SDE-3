#!/bin/bash

# Install Prometheus
sudo apt-get update
sudo apt-get install prometheus

# Install Grafana
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
sudo apt-get update
sudo apt-get install grafana

# Install ELK Stack
sudo apt update
sudo apt install elasticsearch logstash kibana

# Start Services
sudo systemctl start elasticsearch
sudo systemctl start logstash
sudo systemctl start kibana
sudo systemctl start prometheus
sudo systemctl start grafana-server
