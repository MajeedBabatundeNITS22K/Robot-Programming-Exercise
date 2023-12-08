#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize motors and sensors here (if needed).

# Write your program here.
while True:
    # Clear the display
    ev3.screen.clear()

    # Check which buttons are currently pressed
    pressed_buttons = ev3.buttons.pressed()

    # If no buttons are pressed, display 'No button pressed'
    if not pressed_buttons:
        ev3.screen.print("No button pressed")
    else:
        # Display the name of each pressed button
        for button in pressed_buttons:
            ev3.screen.print(button)

    # Check if the center button is pressed and perform an action if needed
    if Button.CENTER in pressed_buttons:
        # Perform the action you want when the center button is pressed
        pass

    # Wait a bit before checking the buttons again
    wait(100)
