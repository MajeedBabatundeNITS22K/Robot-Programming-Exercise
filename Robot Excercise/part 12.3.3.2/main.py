#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)  # Assuming the left motor is connected to port B
right_motor = Motor(Port.C)  # Assuming the right motor is connected to port C

# Initialize the color sensor
CSensor = ColorSensor(Port.S3)

# Start the robot moving forward
left_motor.run(200)  # Adjust the speed if necessary
right_motor.run(200)  # Adjust the speed if necessary

# Continuously check for the red line
while True:
    detected_color = CSensor.color()
    ev3.screen.clear()
    ev3.screen.print("Detected Color: {}".format(detected_color))
    
    # If a red line is detected, stop the robot
    if detected_color == Color.RED:
        left_motor.stop()
        right_motor.stop()
        break  # Exit the loop since the red line is found

    wait(50)  # Check for the color at a fixed rate, adjust as necessary for your robot

# You can add additional code here to make the robot perform other actions after stopping
