#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S2)
touch_sensor = TouchSensor(Port.S1)

# Initialize the drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()

while True:
    # Drive forward at 200 mm/s.
    robot.drive(200, 0)
    
    # If an obstacle is detected within 20 cm, turn 90 degrees
    if ultrasonic_sensor.distance() <= 200:
        robot.stop()
        robot.turn(90)
    
    # If the touch sensor is pressed, exit the loop
    if touch_sensor.pressed():
        break

    wait(10)  # Wait for 10 milliseconds

# Stop the robot
robot.stop()
