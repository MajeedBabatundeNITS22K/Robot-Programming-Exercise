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

# Drive forward at 200 mm/s.
robot.drive(200, 0)

while True:
    # Measure the distance to the nearest object
    distance = ultrasonic_sensor.distance()

    # Play different tones based on the distance
    if distance < 100:  # Less than 10 cm
        ev3.speaker.beep(frequency=880, duration=100)
    elif distance < 200:  # Between 10 cm and 20 cm
        ev3.speaker.beep(frequency=440, duration=100)
    else:  # More than 20 cm
        ev3.speaker.beep(frequency=220, duration=100)

    wait(10)  # Wait for 10 milliseconds to avoid CPU overload
