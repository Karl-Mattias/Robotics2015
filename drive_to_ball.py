from get_ball_coordinates import get_ball_coordinates
from drive_towards import DriveTowards

__author__ = 'Karl'


def drive_to_ball():

	driver = DriveTowards()

	while True:
		coordinates = get_ball_coordinates()
		print("true")
		driver.drive(coordinates)

drive_to_ball()
