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
			#self.motor_controller.stop()
			self.turns_searching += 1
			self.motor_controller.move_back_wheel(60)
			coordinates = self.get_gate_coordinates.get_coordinates()
			print("finding fast")

			# it cannot find gate (might be in the corner)
			# for now just find new ball
			if self.turns_searching > 30:
				break

		# self.motor_controller.stop()

		while self.game_status.status() and self.turns_searching < 30:
			self.turns_searching += 1
			coordinates = self.get_gate_coordinates.get_coordinates()
			print("finding slow")
			if coordinates == -1:
				self.turn()
				break

			x = coordinates[0]
			# closer to looking straight to the gate the smaller the speed
			# speed = (abs(x - 325) / 2)
			# if speed > 20:
			# 	speed = 20

			if x < 310:
				#self.motor_controller.stop()
				self.motor_controller.move_back_wheel(20)
			elif x > 340:
				#self.motor_controller.stop()
				self.motor_controller.move_back_wheel(20 * -1)
			else:  # facing goal
				self.motor_controller.move_right_wheel(60)
				self.motor_controller.move_left_wheel(-60)
				time.sleep(1)
				self.motor_controller.stop()
				break
