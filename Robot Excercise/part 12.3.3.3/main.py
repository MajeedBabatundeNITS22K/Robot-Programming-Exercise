#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)  # Adjust if needed
right_motor = Motor(Port.C)  # Adjust if needed

# Initialize the color sensor
CSensor = ColorSensor(Port.S3)

# Define the notes for different colors
color_notes = {
    Color.RED: 262,    # Middle C
    Color.GREEN: 294,  # D note
    Color.BLUE: 330,   # E note
    Color.YELLOW: 349, # F note
    Color.BROWN: 392,  # G note
    Color.BLACK: 440,  # A note
    Color.WHITE: 494,  # B note
}

# Start the robot moving forward
left_motor.run(200)  # Adjust the speed if necessary
right_motor.run(200)  # Adjust the speed if necessary

# Continuously check for the colors and play corresponding sounds
while True:
    detected_color = CSensor.color()
    ev3.screen.clear()
    ev3.screen.print("Detected Color: {}".format(detected_color))
    
    # Play the note corresponding to the detected color
    if detected_color in color_notes:
        frequency = color_notes[detected_color]
        ev3.speaker.beep(frequency, 500)  # Play the note for 500 milliseconds
    
    # If a red line is detected, stop the robot
    if detected_color == Color.RED:
        left_motor.stop()
        right_motor.stop()
        break  # Stop checking once the red line is found

    wait(50)  # Wait for 50 ms before checking the color again

# You can add additional code here to make the robot perform other actions after stopping
