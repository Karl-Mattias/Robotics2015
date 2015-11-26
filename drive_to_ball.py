from get_coordinates import GetCoordinates
from drive_towards import DriveTowards
from turn_to_goal import TurnToGoal
# from settings import BoltSettings
__author__ = 'Karl'


class DriveController(object):

	def __init__(self, mainboard_controller, motor_controller, referee_module):
		# bolt_settings = BoltSettings().read_dict()
		self.get_coordinates = GetCoordinates()
		self.driver = DriveTowards(mainboard_controller, motor_controller)
		self.to_goal = TurnToGoal(mainboard_controller, motor_controller, referee_module, self.get_coordinates)
		self.i = 0
		self.referee_module = referee_module
		self.motor_controller = motor_controller
		self.mainboard_controller = mainboard_controller

	def drive_to_ball(self):

		while self.referee_module.game_status():
			# self.mainboard_controller.charge()
			ball_coordinates = self.get_coordinates.get_coordinates("ball")
			# goal_coordinates = self.get_goal_coordinates.get_coordinates()
			# print("i = " + str(self.i))
			self.mainboard_controller.ping()
			self.mainboard_controller.start_dribbler()  # just in case the dribbler did not start

			if ball_coordinates != -1 or self.mainboard_controller.has_ball():

				if self.mainboard_controller.has_ball():
					print("has ball")
					self.motor_controller.stop()
					self.to_goal.turns_searching = 0
					self.to_goal.turn()
					continue

				# y_ball = ball_coordinates[1]
				# not working this way
				'''if goal_coordinates != -1 and goal_coordinates[1] < y_ball + 5:
					print("goal too close!")
					self.driver.circle()'''

				if self.i > 5:
					self.motor_controller.stop()

				self.driver.drive(ball_coordinates)
				self.i = 0

			else:
				# to avoid cases when just losing the blob for one frame
				self.i += 1
				if self.i > 5:
					self.driver.circle()

	def kill(self):
		self.get_coordinates.kill()
