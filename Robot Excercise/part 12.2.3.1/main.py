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
left_motor = Motor(Port.C)  # Assuming the left motor is connected to Port C
right_motor = Motor(Port.B)  # Assuming the right motor is connected to Port B

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Parameters for the square.
side_length = 300  # Adjust this based on the desired size of the square
turn_angle = 90    # degrees

# Drive in a square.
for _ in range(4):
    # Drive forward for the length of one side of the square.
    robot.straight(side_length)
    
    # Turn 90 degrees.
    robot.turn(turn_angle)

# Stop the robot.
robot.stop()