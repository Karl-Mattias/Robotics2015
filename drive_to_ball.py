import time
from get_ball_coordinates import get_ball_coordinates
from drive_towards import DriveTowards
from motor_controller import MotorController

__author__ = 'Karl'


def drive_to_ball():

	coordinates = get_ball_coordinates()
	driver = DriveTowards()
	motor_controller = MotorController()

	while coordinates != -1:
		coordinates = get_ball_coordinates()
		driver.drive(coordinates)
		time.sleep(0.5)
		motor_controller.stop()

drive_to_ball()