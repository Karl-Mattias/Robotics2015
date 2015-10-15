from get_ball_coordinates import get_ball_coordinates
from drive_towards import DriveTowards

__author__ = 'Karl'


def drive_to_ball():

	coordinates = get_ball_coordinates()
	driver = DriveTowards()

	while coordinates != -1:
		coordinates = get_ball_coordinates()
		driver.drive(coordinates)

drive_to_ball()
