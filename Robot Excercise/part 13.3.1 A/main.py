#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umqtt.robust import MQTTClient
import time

# Create your objects here.
ev3 = EV3Brick()

# Initialize the MQTT client for Robot A
MQTT_ClientID = 'robot_a'
MQTT_Broker = '192.168.189.184'  # IP of the MQTT Broker
MQTT_Topic_Status = 'Lego/Status'

# Callback function to process incoming messages
def on_message(topic, msg):
    if topic == MQTT_Topic_Status.encode():
        message = msg.decode()
        ev3.screen.print(message)

# Setup MQTT client
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)
client.set_callback(on_message)
client.connect()
client.subscribe(MQTT_Topic_Status)

# Indicate that Robot A has started
ev3.screen.print('Started')
client.publish(MQTT_Topic_Status, 'Robot A is listening')
time.sleep(0.5)

# Main loop to listen for messages
try:
    while True:
        client.check_msg()
        time.sleep(0.5)
except KeyboardInterrupt:
    client.disconnect()

# Add any additional code or functions below if necessary
