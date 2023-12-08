#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# Initialize the motors.
left_motor = Motor(Port.C)  # Assuming the left motor is connected to Port C
right_motor = Motor(Port.B)  # Assuming the right motor is connected to Port B

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Acceleration parameters
initial_speed = 0  # Starting speed in mm/s
max_speed = 500    # Maximum speed in mm/s
acceleration = 50  # Speed increase each second in mm/s
duration = 1000    # Duration for each speed increment in ms (1 second)

# Gradual acceleration
current_speed = initial_speed
while current_speed <= max_speed:
    robot.drive(current_speed, 0)
    wait(duration)
    current_speed += acceleration

# Stop the robot.
robot.stop()