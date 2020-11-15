import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.168.137.189",1883,60)
client.publish("topic", "HEmant Purvi Class Lab");
client.disconnect();
