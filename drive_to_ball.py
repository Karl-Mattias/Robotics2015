from get_coordinates import GetCoordinates
from drive_towards import DriveTowards
from turn_to_goal import TurnToGoal

__author__ = 'Karl'


def drive_to_ball():

	get_ball_coordinates = GetCoordinates("ball")
	driver = DriveTowards()
	to_goal = TurnToGoal()

	while True:
		coordinates = get_ball_coordinates.get_coordinates()
		driver.drive(coordinates)

		if coordinates[1] < 25:
			to_goal.turn()
			break

drive_to_ball()
