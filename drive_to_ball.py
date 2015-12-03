from get_coordinates import GetCoordinates
from turn_to_goal import TurnToGoal
from drive_to_goal import drive_to_goal
__author__ = 'Karl'


class DriveToBall(object):

	def __init__(self, mainboard_controller, drive_controller, referee_module):
		self.get_coordinates = GetCoordinates()
		self.drive_controller = drive_controller
		self.to_goal = TurnToGoal(mainboard_controller, drive_controller, referee_module, self.get_coordinates)
		self.i = 0
		self.referee_module = referee_module
		self.mainboard_controller = mainboard_controller

	def drive_to_ball(self):

		while self.referee_module.game_status():
			coordinates = self.get_coordinates.get_coordinates()
			ball_coordinates = coordinates["ball"]
			self.mainboard_controller.ping()
			self.mainboard_controller.start_dribbler()  # just in case the dribbler did not start

			if ball_coordinates != -1 or self.mainboard_controller.has_ball():

				if self.mainboard_controller.has_ball():
					print("has ball")
					self.drive_controller.stop()
					self.to_goal.turns_searching = 0
					self.to_goal.turn()
					continue

				# y_ball = ball_coordinates[1]
				# not working this way
				'''if goal_coordinates != -1 and goal_coordinates[1] < y_ball + 5:
					print("goal too close!")
					self.driver.circle()'''

				black_coordinates = coordinates["black"]

				if black_coordinates != -1 and black_coordinates[3] > 400 and black_coordinates[2] > 400:
					print("darkness ahead")

				if self.i > 5:
					self.drive_controller.stop()

				self.drive_controller.drive(ball_coordinates)
				self.i = 0

			else:
				# to avoid cases when just losing the blob for one frame
				self.i += 1
				if self.i > 3:
					self.drive_controller.circle()

				if self.i > 15:
					drive_to_goal(self.get_coordinates, self.drive_controller)
