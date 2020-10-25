#!/usr/bin/env python

import uuid
import time
import random as rnd

import sample_data_pb2 as protobufData

import paho.mqtt.client as mqtt_client
import paho.mqtt.publish as publish


def callbackOnConnect(client, userdata, flags, rc):
    """Callback when connected"""
    print(f"Connected to: {rc}")


if __name__=="__main__":
    while True:
        # -- generate protobuf value
        dataset = protobufData.Data()
        dataset.id = uuid.uuid4().hex
        dataset.value = rnd.randint(5, 100)
        print(dataset.id, dataset.value)
        if dataset.IsInitialized():
            protobuf_payload = dataset.SerializeToString()
        # --
        else:
            continue
        # --
        publish.single(
            topic="paho/testSampledata/single",
            payload=protobuf_payload,
            retain=True,
            port=1883,
            hostname="localhost",
            keepalive=10
        )
        print(f"Sending Payload: {protobuf_payload}")
        time.sleep(5)