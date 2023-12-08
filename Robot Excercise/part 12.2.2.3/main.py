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
left_motor = Motor(Port.B)   # Assuming the left motor is connected to Port B
right_motor = Motor(Port.C)  # Assuming the right motor is connected to Port C

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Drive parameters.
drive_speed = 100  # mm/s
drive_time = 2000  # ms (Adjust this based on the size of the square you want)
turn_angle = 90    # degrees

# Drive in a square.
for _ in range(4):
    # Drive forward.
    robot.drive_time(drive_speed, 0, drive_time)
    wait(drive_time)
    
    # Turn right by 90 degrees.
    robot.turn(turn_angle)
    wait(1000)  # Wait for a short time after the turn.

# Stop the robot.
robot.stop()
