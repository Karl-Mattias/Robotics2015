from settings import BoltSettings
from time import sleep

__author__ = 'Karl'


class TurnToGoal:
	def __init__(self, mainboard_controller, motor_controller, referee_module, get_coordinates):
		self.get_gate_coordinates = get_coordinates
		self.motor_controller = motor_controller
		self.referee_module = referee_module
		self.mainboard_controller = mainboard_controller
		self.turns_searching = 0

	def turn(self):

		bolt_settings = BoltSettings().read_dict()

		coordinates = self.get_gate_coordinates.get_coordinates()
		opponent_coordinates = coordinates[bolt_settings["opponent_goal_color"]]
		self_coordinates = coordinates[bolt_settings["own_goal_color"]]

		self_x = self_coordinates[0]
		opponent_x = opponent_coordinates[0]

		if opponent_x + 10 > self_x > 10 - opponent_x:  # The colours are of a robot not of a gate
			opponent_coordinates = -1

		while opponent_coordinates == -1 and self.referee_module.game_status() and self.mainboard_controller.has_ball():
			self.mainboard_controller.ping()
			self.turns_searching += 1
			self.motor_controller.move_back_wheel(50)
			opponent_coordinates = self.get_gate_coordinates.get_coordinates()[bolt_settings["opponent_goal_color"]]
			print("finding fast: " + str(opponent_coordinates))

			# it cannot find gate (might be in the corner)
			# for now just find new ball
			if self.turns_searching > 15:
				break

		self.motor_controller.stop()

		in_this = 0
		while self.referee_module.game_status() and self.mainboard_controller.has_ball():
			self.mainboard_controller.ping()
			in_this += 1
			coordinates = self.get_gate_coordinates.get_coordinates()
			opponent_coordinates = coordinates[bolt_settings["opponent_goal_color"]]
			print("finding slow: " + str(opponent_coordinates))
			if opponent_coordinates == -1:
				if in_this < 5:
					continue
				self.turn()
				break
			self_coordinates = coordinates[bolt_settings["own_goal_color"]]
			self_x = self_coordinates[0]
			opponent_x = opponent_coordinates[0]

			if opponent_x + 10 > self_x > 10 - opponent_x:  # The colours are of a robot not of a gate
				if in_this < 5:
					continue
				self.turn()
				break

			width = opponent_coordinates[2]
			# print("width: " + str(width))
			# closer to looking straight to the gate the smaller the speed
			# speed = (abs(x - 325) / 2)
			# if speed > 20:
			# 	speed = 20

			if opponent_x < 350 - width/4:
				self.motor_controller.move_back_wheel(20)
			elif opponent_x > 350 + width/4:
				self.motor_controller.move_back_wheel(20 * -1)
			else:  # facing goal
				print("facing!")
				self.motor_controller.stop()
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
				break
