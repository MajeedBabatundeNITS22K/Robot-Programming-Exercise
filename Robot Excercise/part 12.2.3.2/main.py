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

# Parameters for the figure "8".
turn_angle = 360  # degrees for a full circle; adjust as needed
drive_speed = 100  # mm/s
turn_rate = 50     # degrees/s; positive for right turn, negative for left turn

# First half of the figure "8": right loop
robot.drive_time(drive_speed, turn_rate, 2000)  # Adjust time for the size of the loop
wait(2000)  # Wait for the first loop to complete

# Second half of the figure "8": left loop
robot.drive_time(drive_speed, -turn_rate, 2000)  # Adjust time for the size of the loop
wait(2000)  # Wait for the second loop to complete

# Stop the robot.
robot.stop()