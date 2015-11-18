from get_coordinates import GetCoordinates
from motor_controller import MotorController
from settings import BoltSettings
from game_status import GameStatus
from mainboard_controller import MainBoardController
from time import sleep

__author__ = 'Karl'


class TurnToGoal:
	def __init__(self):
		bolt_settings = BoltSettings().read_dict()
		self.get_gate_coordinates = GetCoordinates(bolt_settings["opponent_goal_color"])
		self.motor_controller = MotorController()
		self.game_status = GameStatus()
		self.mainboard_controller = MainBoardController()
		self.turns_searching = 0

	def turn(self):

		coordinates = self.get_gate_coordinates.get_coordinates()
		while coordinates == -1 and self.game_status.status():
			self.mainboard_controller.ping()
			self.turns_searching += 1
			self.motor_controller.move_back_wheel(40)
			coordinates = self.get_gate_coordinates.get_coordinates()
			print("finding fast: " + str(coordinates))

			# it cannot find gate (might be in the corner)
			# for now just find new ball
			if self.turns_searching > 15:
				break

		self.motor_controller.stop()

		in_this = 0
		while self.game_status.status():
			self.mainboard_controller.ping()
			in_this += 1
			coordinates = self.get_gate_coordinates.get_coordinates()
			self.mainboard_controller.charge()
			print("finding slow: " + str(coordinates))
			if coordinates == -1:
				if in_this < 5:
					continue
				self.turn()
				break

			x = coordinates[0]
			width = coordinates[2]
			# print("width: " + str(width))
			# closer to looking straight to the gate the smaller the speed
			# speed = (abs(x - 325) / 2)
			# if speed > 20:
			# 	speed = 20

			if x < 350 - width/4:
				self.motor_controller.move_back_wheel(20)
			elif x > 350 + width/4:
				self.motor_controller.move_back_wheel(20 * -1)
			else:  # facing goal
				print("facing!")
				# self.mainboard_controller.charge()
				self.motor_controller.stop()
				self.mainboard_controller.kick()
				if self.mainboard_controller.has_ball():
					sleep(0.5)
					print("kick again")
					self.mainboard_controller.kick()
				break
