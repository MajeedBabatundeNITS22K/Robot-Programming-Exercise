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

# Initial greetings
ev3.speaker.beep()
ev3.screen.print("Hello World!")
time.sleep(4)

# Define motors and robot drive base
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Define touch sensor
TSensor = TouchSensor(Port.S3)

def play_sound():
    ev3.speaker.beep()

def stop_sound():
    ev3.speaker.beep(frequency=0, duration=0)

start_time = time.time()  # Record the start time
last_pressed = False  # To check for a state change

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:  # Check if 1 minute has passed
        break

    is_pressed = TSensor.pressed()
    
    if is_pressed and not last_pressed:  # Check if the state has changed to pressed
        play_sound()
        # Driving logic when the button is pressed
        robot.straight(300)
        robot.turn(90)
        robot.drive(125, 40)

    elif not is_pressed:
        stop_sound()

    last_pressed = is_pressed  # Update the last state
