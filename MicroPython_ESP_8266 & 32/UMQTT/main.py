
pin = machine.Pin(2,machine.Pin.OUT)
lights = machine.Pin(23,OUT)
fan = machine.Pin(22,OUT)

def callback(topic,message):
  print(topic,message)
  if message == b'on':
    pin.value(True)
  if message==b'off':
    pin.value(False)
  # lights 
  if message == b'lightson':
    lights.value(True)
  if message==b'lightsoff':
    lights.value(False)
  #Fan
  if message == b'fanon':
    fan.value(True)
  if message==b'fanoff':
    fan.value(False)
   
  else :
    print(message)
      
    
broker_address = '192.168.137.173'
client_id = 'esp32_{}'.format(ubinascii.hexlify(machine.unique_id()))
topic = b'lights'


client = MQTTClient(client_id,broker_address)
client.set_callback(callback)
client.connect()
client.subscribe(topic)
while True:
  client.wait_msg()
  

