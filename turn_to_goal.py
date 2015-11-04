from get_coordinates import GetCoordinates
from motor_controller import MotorController
from settings import BoltSettings
from game_status import GameStatus
import time

__author__ = 'Karl'


class TurnToGoal:
	def __init__(self):
		bolt_settings = BoltSettings().read_dict()
		self.get_gate_coordinates = GetCoordinates(bolt_settings["opponent_goal_color"])
		self.motor_controller = MotorController()
		self.game_status = GameStatus()

	def turn(self):

		coordinates = self.get_gate_coordinates.get_coordinates()
		while coordinates == -1:
			self.motor_controller.stop()
			self.motor_controller.move_back_wheel(60)
			coordinates = self.get_gate_coordinates.get_coordinates()

		while self.game_status.status():
			coordinates = self.get_gate_coordinates.get_coordinates()
			if coordinates == -1:
				continue

			x = coordinates[0]
			# closer to looking straight to the gate the smaller the speed
			# speed = (abs(x - 325) / 2)
			# if speed > 20:
			# 	speed = 20

			if x < 320:
				#self.motor_controller.stop()
				self.motor_controller.move_back_wheel(20)
			elif x > 330:
				#self.motor_controller.stop()
				self.motor_controller.move_back_wheel(20 * -1)
			else:
				break

		#self.motor_controller.stop()
		self.motor_controller.move_right_wheel(100)
		self.motor_controller.move_left_wheel(-100)
		time.sleep(1)
		self.motor_controller.stop()
