# Readme

## MQTT Tests

Repository to test how MQTT works with python and the ways to publish and subscribe to data in the broker.

### How To:

1. Run the docker-image by using `docker-compose up`
2. In case you need to update protocol-buffer type
    - Run `protoc -I=./ --python_out=./ ./sample_data.proto`
    - This will create the `sample_data_pb2.py` file from which you required data-class can be imported
2. Run the publisher by using `python publisher.py`
    - The publisher will print out the payload it sends
3. Run the subscriber by using `python subscriber.py`
    - The subscriber will print out the payload it receives

### Things to do:

- Play around with the configurations and the payloads
- Look into broker QoS values in the configuration

## TCP Socket Low-Level

To do

## Tornado Server-Client

To do

