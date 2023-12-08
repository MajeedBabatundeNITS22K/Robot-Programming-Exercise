#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#!/usr/bin/env pybricks-micropython
from umqtt.robust import MQTTClient
import time

# Initialize the MQTT client for Robot B
MQTT_ClientID = 'robot_b'
MQTT_Broker = '192.168.189.184'  # IP of the MQTT Broker, should be the same as for Robot A
MQTT_Topic_Status = 'Lego/Status'

# Setup MQTT client
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)
client.connect()
time.sleep(0.5)

# Send the "Hello World!" message
client.publish(MQTT_Topic_Status, 'Hello World!')
time.sleep(0.5)

# Disconnect after sending the message
client.disconnect()