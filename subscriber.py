import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    """Callback when client receives CONNACK response from the server"""
    print("Connected with result code " + str(rc))

    client.subscribe("paho/testSampledata/single")

def on_message(client, userdata, msg):
    """Callback for when a published message is received from a server"""
    print(msg.topic + " " + str(msg.payload))

# 00
if __name__=="__main__":
    client = mqtt.Client(client_id="45")
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    
    client.loop_forever()

