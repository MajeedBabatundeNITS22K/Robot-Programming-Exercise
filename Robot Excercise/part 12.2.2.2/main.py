#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
# Initialize the motors.
left_motor = Motor(Port.B)   # Assuming the left motor is connected to Port B
right_motor = Motor(Port.C)  # Assuming the right motor is connected to Port C

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Set the drive speed at 100 millimeters per second and the turn rate at 30 degrees per second.
# The positive turn rate makes the robot turn left, thus driving in a circle.
robot.drive(100, 30)

# Let the robot drive in a circle for 5 seconds.
wait(5000)

# Stop the robot.
robot.stop()