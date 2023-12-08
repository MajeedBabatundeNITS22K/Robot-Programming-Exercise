#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize motors, color sensor, and touch sensor.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Initialize counters for colors.
color_counters = {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 0, Color.YELLOW: 0, Color.BLACK: 0, Color.BROWN: 0, Color.WHITE: 0}
line_counter = 0
color_sequence = []
last_color = None  # Variable to remember the last color seen.

# Define a mapping for colors to tones (frequencies).
color_tones = {
    Color.RED: 262,    # C note
    Color.GREEN: 294,  # D note
    Color.BLUE: 330,   # E note
    Color.YELLOW: 349, # F note
    Color.BLACK: 392,  # G note
    Color.BROWN: 440,  # A note
    Color.WHITE: 494,  # B note
}

# Start moving the robot forward.
robot.drive(100, 0)

while not touch_sensor.pressed():
    # Read the detected color from the color sensor.
    detected_color = color_sensor.color()

    # Check if a new color line is crossed.
    if detected_color is not None and detected_color != last_color:
        line_counter += 1
        color_counters[detected_color] += 1
        color_sequence.append(detected_color)
        last_color = detected_color  # Update the last seen color.

        # Update the display with the current count of lines.
        ev3.screen.clear()
        ev3.screen.print("Total lines: {}".format(line_counter))
        for color, count in color_counters.items():
            ev3.screen.print("{}: {}".format(color, count))
        
    # Wait for a short period to prevent the loop from running too fast.
    wait(100)

robot.stop()

# Now switch to output mode and play tones in the order of recognized colors.
for color in color_sequence:
    tone = color_tones.get(color, 440)  # Default to 440 Hz (A note) if color not in dictionary.
    ev3.speaker.beep(tone, 500)
    wait(500)  # Wait between tones.
