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

# Parameters
forward_speed = 200  # Fast forward speed in mm/s
backward_speed = -100  # Slow backward speed in mm/s
distance = 1000  # Distance to travel in mm (1 meter)

# Drive forward quickly for 1 meter.
robot.drive_time(forward_speed, 0, distance / forward_speed * 1000)
wait(distance / forward_speed * 1000)

# Stop and wait for 2 seconds, then play a tone.
ev3.speaker.play_tone(440, 500)  # Play a 440 Hz tone for 500 ms
wait(2000)

# Drive backward slowly to the starting point.
robot.drive_time(backward_speed, 0, distance / abs(backward_speed) * 1000)
wait(distance / abs(backward_speed) * 1000)

# Stop the robot.
robot.stop()