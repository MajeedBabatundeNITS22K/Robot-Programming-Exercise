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

# Initialize motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Setup MQTT for communication
MQTT_ClientID = 'robot_b'
MQTT_Broker = '192.168.43.113'
MQTT_Topic = 'Lego/Command'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)
client.connect()
ev3.speaker.beep()

# Callback function to process incoming messages.
def on_message(topic, msg):
    if topic == MQTT_Topic.encode() and msg == b'start':
        # Start driving when the 'start' message is received.
        robot.drive(100, 0)

# Set the callback function before subscribing.
client.set_callback(on_message)

# Subscribe to the topic.
client.subscribe(MQTT_Topic)

# Loop to keep listening for messages.
try:
    while True:
        client.check_msg()
        # Short delay to prevent flooding the network.
        time.sleep(0.1)
except KeyboardInterrupt:
    # Stop the robot if an interrupt is received (like Ctrl+C)
    robot.stop()
finally:
    # Ensure the robot stops driving and the client disconnects cleanly in any case.
    robot.stop()
    client.disconnect()