import paho.mqtt.client as mqtt #import the client1
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
time.sleep(2)   
def on_log(client, userdata, level, buf):
    print("log: ",buf)
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    if int(message.payload.decode("utf-8")) > 45:
        ser.write('1') # prefix b is required for Python 3.x, optional for Python 2.x
    else:
        ser.write('0')
########################################
broker_address="spica.eic.cefet-rj.br"
print("creating new instance")
client1 = mqtt.Client("P1") #create new instance
#client.on_log=on_log#attach function to log
client1.on_message=on_message #attach function to callback
print("connecting to broker")
client1.username_pw_set("aluno", "aluno")
client1.connect(broker_address) #connect to broker
client1.loop_start() #start the loop
print("Subscribing to topic","temperatura")
client1.subscribe("temperatura")
print("Publishing message to topic","temperatura")
client1.publish("temperatura","46")
time.sleep(4) # wait
client1.loop_stop() #stop the loop
print("creating new instance")


client2 = mqtt.Client("P2") #create new instance
#client.on_log=on_log#attach function to log
client2.on_message=on_message #attach function to callback
print("connecting to broker")
client2.username_pw_set("aluno", "aluno")
client2.connect(broker_address) #connect to broker
client2.loop_start() #start the loop
print("Subscribing to topic","temperatura")
client2.subscribe("temperatura")
print("Publishing message to topic","temperatura")
client2.publish("temperatura","20")
time.sleep(4) # wait
client2.loop_stop() #stop the loop

