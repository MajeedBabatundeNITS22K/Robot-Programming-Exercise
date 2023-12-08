#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the color sensor
CSensor = ColorSensor(Port.S3)

# Define a dictionary to map color codes to color names
color_names = {
    Color.BLACK: "Black",
    Color.BLUE: "Blue",
    Color.GREEN: "Green",
    Color.YELLOW: "Yellow",
    Color.RED: "Red",
    Color.WHITE: "White",
    Color.BROWN: "Brown",
}

# Continuously detect and display color
while True:
    # Get the detected color
    detected_color = CSensor.color()

    # Clear the screen
    ev3.screen.clear()

    # Print the detected color name
    if detected_color is None:
        ev3.screen.print("Detected Color: No color")
    else:
        ev3.screen.print("Detected Color: {}".format(color_names.get(detected_color, "Unknown")))

    # Wait for a short period before updating the display
    wait(500)
