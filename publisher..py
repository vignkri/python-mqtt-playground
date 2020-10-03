#!/usr/bin/env python

import uuid
import time
import random as rnd

import paho.mqtt.client as mqtt_client
import paho.mqtt.publish as publish


def callbackOnConnect(client, userdata, flags, rc):
    """Callback when connected"""
    print(f"Connected to: {rc}")


if __name__=="__main__":
    while True:
        _payload = str(dict(
                id=str(uuid.uuid4().hex),
                value=rnd.randint(5, 100)
            ))
        publish.single(
            topic="paho/testSampledata/single",
            payload=_payload,
            retain=True,
            port=1883,
            hostname="localhost",
            keepalive=10
        )
        print(f"Sending Payload: {_payload}")
        time.sleep(5)