#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, UltrasonicSensor)
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Initialize the drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Set the drive speed at 200 mm/s.
robot.drive(200, 0)

# Drive forward until the ultrasonic sensor sees an obstacle within 20 cm.
while ultrasonic_sensor.distance() > 200:
    wait(10)  # Wait for 10 milliseconds

# Stop the robot
robot.stop()
