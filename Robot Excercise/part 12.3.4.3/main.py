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

# Function to play a tone based on the button pressed
def play_tone(button):
    if button == Button.UP:
        ev3.speaker.play_tone(262, 500)  # C note
    elif button == Button.DOWN:
        ev3.speaker.play_tone(294, 500)  # D note
    elif button == Button.LEFT:
        ev3.speaker.play_tone(330, 500)  # E note
    elif button == Button.RIGHT:
        ev3.speaker.play_tone(349, 500)  # F note
    elif button == Button.CENTER:
        ev3.speaker.play_tone(392, 500)  # G note

# Main loop
while True:
    pressed_buttons = ev3.buttons.pressed()

    for button in pressed_buttons:
        play_tone(button)

    wait(100)  # Small delay to prevent excessive polling

# Stop the robot (if needed).
robot.stop()