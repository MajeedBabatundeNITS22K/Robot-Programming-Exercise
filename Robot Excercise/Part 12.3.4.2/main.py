#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Write your program here.
while True:
    # Check if the center button is currently pressed
    if Button.CENTER in ev3.buttons.pressed():
        # If the center button is pressed, turn the light red
        ev3.light.on(Color.RED)
    else:
        # If the center button is not pressed, turn the light green
        ev3.light.on(Color.GREEN)
    
    # Wait a bit before checking the button again to prevent bouncing
    wait(50)
