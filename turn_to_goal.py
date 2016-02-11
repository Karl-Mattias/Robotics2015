from settings import BoltSettings
from drive_to_goal import drive_to_goal
from time import sleep

__author__ = 'Karl'


class TurnToGoal:
	def __init__(self, mainboard_controller, drive_controller, referee_module, get_coordinates):
		self.get_coordinates = get_coordinates
		self.drive_controller = drive_controller
		self.referee_module = referee_module
		self.mainboard_controller = mainboard_controller
		self.turns_searching = 0

	def turn(self):

		goal_coordinates = self.get_goal_coordinates()

		while goal_coordinates == -1 and self.referee_module.game_status() and self.mainboard_controller.has_ball():
			self.mainboard_controller.ping()
			self.turns_searching += 1
			self.drive_controller.around_ball(-5)
			goal_coordinates = self.get_goal_coordinates()

			# it cannot find gate (might be in the corner)
			if self.turns_searching > 15:
				drive_to_goal(self.get_coordinates, self.drive_controller, self.mainboard_controller)

		self.drive_controller.stop()

		in_this = 0
		while self.referee_module.game_status() and self.mainboard_controller.has_ball():
			self.mainboard_controller.ping()
			in_this += 1
			goal_coordinates = self.get_goal_coordinates()

			if goal_coordinates == -1:
				if in_this < 2:
					continue
				self.turn()
				break

			if in_this > 5:  # searching for the gate too long already
				print("Searched for too long")
				self.kick()

			opponent_x = goal_coordinates[0]
			width = goal_coordinates[2]

			if opponent_x < 350 - width/4:
				self.drive_controller.around_ball(2)
			elif opponent_x > 350 + width/4:
				self.drive_controller.around_ball(-2)
			else:  # facing goal
				print("facing!")
				self.drive_controller.stop()
				self.kick()
				break

	def get_goal_coordinates(self):
		bolt_settings = BoltSettings().read_dict()

		coordinates = self.get_coordinates.get_coordinates()
		opponent_coordinates = coordinates[bolt_settings["opponent_goal_color"]]
		self_coordinates = coordinates[bolt_settings["own_goal_color"]]

		if self_coordinates != -1 and opponent_coordinates != -1:
			self_x = self_coordinates[0]
			opponent_x = opponent_coordinates[0]

			if opponent_x + 10 > self_x > 10 - opponent_x:  # The colours are of a robot not of a gate
				opponent_coordinates = -1

		return opponent_coordinates

	def kick(self):
		print("kick")
		self.mainboard_controller.kick()
		sleep(0.5)
		self.mainboard_controller.ping()

		if self.mainboard_controller.has_ball():
			print("still having ball")
			self.mainboard_controller.charge()
			sleep(1)
			self.mainboard_controller.ping()
			sleep(1)
			self.mainboard_controller.ping()
			sleep(1)
			print("kick again")
			self.mainboard_controller.kick()
