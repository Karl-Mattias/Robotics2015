from get_coordinates import GetCoordinates
from drive_towards import DriveTowards
from turn_to_goal import TurnToGoal
from game_status import GameStatus
from motor_controller import MotorController
from settings import BoltSettings
# from mainboard_controller import MainBoardController
__author__ = 'Karl'


class DriveController(object):

	def __init__(self):
		bolt_settings = BoltSettings().read_dict()
		self.get_ball_coordinates = GetCoordinates("ball")
		self.get_goal_coordinates = GetCoordinates(bolt_settings["opponent_goal_color"])
		self.driver = DriveTowards()
		self.to_goal = TurnToGoal()
		self.i = 0
		self.game_status = GameStatus()
		self.motor_controller = MotorController()
		# self.mainboard_controller = MainBoardController()

	def drive_to_ball(self, mainboard_controller):

		while self.game_status.status():
			ball_coordinates = self.get_ball_coordinates.get_coordinates()
			# goal_coordinates = self.get_goal_coordinates.get_coordinates()
			# print("i = " + str(self.i))
			mainboard_controller.ping()
			mainboard_controller.start_dribbler()  # just in case the dribbler did not start

			if ball_coordinates != -1 or mainboard_controller.has_ball():

				if mainboard_controller.has_ball():
					print("has ball")
					self.motor_controller.stop()
					self.to_goal.turns_searching = 0
					self.to_goal.turn()
					continue

				y_ball = ball_coordinates[1]
				# not working this way
				'''if goal_coordinates != -1 and goal_coordinates[1] < y_ball + 5:
					print("goal too close!")
					self.driver.circle()'''

				if self.i > 5:
					self.motor_controller.stop()

				self.driver.drive(ball_coordinates)
				self.i = 0

			else:
				mainboard_controller.charge()
				# to avoid cases when just losing the blob for one frame
				self.i += 1
				if self.i > 5:
					self.driver.circle()

	def kill(self):
		self.get_ball_coordinates.kill()
