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
		self.turns_searching = 0

	def turn(self):

		coordinates = self.get_gate_coordinates.get_coordinates()
		while coordinates == -1 and self.game_status.status():
			self.turns_searching += 1
			self.motor_controller.move_back_wheel(60)
			coordinates = self.get_gate_coordinates.get_coordinates()
			print("finding fast")

			# it cannot find gate (might be in the corner)
			# for now just find new ball
			if self.turns_searching > 30:
				break

		self.motor_controller.stop()

		in_this = 0
		while self.game_status.status() and self.turns_searching < 30:
			in_this += 1
			self.turns_searching += 1
			coordinates = self.get_gate_coordinates.get_coordinates()
			print("finding slow")
			if coordinates == -1:
				if in_this < 5:
					continue
				self.turn()
				break

			x = coordinates[0]
			width = coordinates[2]
			print("width: " + str(width))
			# closer to looking straight to the gate the smaller the speed
			# speed = (abs(x - 325) / 2)
			# if speed > 20:
			# 	speed = 20

			if x < 350 - width/4:
				self.motor_controller.move_back_wheel(20)
			elif x > 350 + width/4:
				self.motor_controller.move_back_wheel(20 * -1)
			else:  # facing goal
				self.motor_controller.stop()
				self.motor_controller.move_right_wheel(70)
				self.motor_controller.move_left_wheel(-70)
				time.sleep(1)
				self.motor_controller.stop()
				break
