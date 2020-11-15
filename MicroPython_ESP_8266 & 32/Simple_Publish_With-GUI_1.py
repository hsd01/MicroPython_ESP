import paho.mqtt.publish as pub
import time
from tkinter import *

root = Tk()
root.title("    MQTT    ")
root.geometry("300x300")
hostname = '192.168.137.173'


def on():
    print("Sending 1 to topic:")
    #pub.single("TOPIC","message", hostname ="192.168.173.137")
    pub.single("esp8266","1", hostname)# ="192.168.137.162")
    #time.sleep(2)

def off():
    print("Sending 0 to topic:")
    pub.single("esp8266","0", hostname)# ="192.168.137.162")
    #time.sleep(2)

lbl = Label(root,text="Welcome to MQTT",font=("Arial Bold",18)).grid(column=0,row=0)
btn1 = Button(root, text = 'ON',command = on).grid(column = 4, row = 3)
btn2 = Button(root, text = 'OFF',command = off).grid(column = 4, row = 6)

root.mainloop()
