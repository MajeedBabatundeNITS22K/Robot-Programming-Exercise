#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from umqtt.robust import MQTTClient


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize motors and ultrasonic sensor.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
sensor = UltrasonicSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Setup MQTT for communication
MQTT_ClientID = 'robot_a'
MQTT_Broker = '192.168.43.113'
MQTT_Topic = 'Lego/Command'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)
client.connect()
ev3.speaker.beep()

# Start moving towards Robot B
robot.drive(100, 0)

# Keep moving until the robot is close to Robot B
while sensor.distance() > 200:  # adjust distance as needed
    pass

# Stop Robot A
robot.stop()

# Send message to Robot B to start moving
client.publish(MQTT_Topic, 'start')

# Disconnect MQTT client
client.disconnect()