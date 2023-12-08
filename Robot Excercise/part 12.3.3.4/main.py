#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
color_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Define the speeds for the robot.
current_speed = 200  # Current speed of the robot
standard_speed = 200  # Standard speed for the robot
slower_speed = 100    # Slower speed for when the robot is on blue

# The reflection threshold between the black line and the floor.
black_threshold = 10

# The reflection threshold for detecting the blue color.
blue_threshold = 25

# Start moving the robot forward at the standard speed.
robot.drive(standard_speed, 0)

while True:
    # Read the reflection value from the color sensor.
    reflection = color_sensor.reflection()

    # Check the detected color.
    detected_color = color_sensor.color()

    # Stop if the sensor detects red.
    if detected_color == Color.RED:
        robot.stop()
        break
    
    # If the sensor detects blue, reduce speed.
    if detected_color == Color.BLUE:
        if current_speed != slower_speed:
            current_speed = slower_speed
            robot.drive(current_speed, 0)
    else:
        # If the sensor detects colors other than blue, use the standard speed.
        if current_speed != standard_speed:
            current_speed = standard_speed
            robot.drive(current_speed, 0)
    
    # Calculate the deviation from the threshold.
    deviation = black_threshold - reflection
    
    # Calculate the turn rate based on the deviation.
    turn_rate = deviation * 2  # The "2" is a gain value that might need tuning.

    # Update the turn rate while maintaining the current speed.
    robot.drive(current_speed, turn_rate)

    # Wait for a short period to prevent the loop from running too fast.
    wait(10)

# Add a beep to indicate that we've stopped.
ev3.speaker.beep()
