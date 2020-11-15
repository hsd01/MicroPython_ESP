import paho.mqtt.publish as pub
import time

while True:
    print("Sending 1 to topic:")
    #pub.single("TOPIC","message", hostname ="192.168.173.137")
    pub.single("ESP32","1", hostname ="192.168.173.137")
    time.sleep(2)
    print("Sending 0 to topic:")
    pub.single("ESP32","0", hostname ="192.168.173.137")
    time.sleep(2)
