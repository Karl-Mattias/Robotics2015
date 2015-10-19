from get_coordinates import GetCoordinates
from motor_controller import MotorController
import time

__author__ = 'Karl'


class TurnToGoal:

	def __init__(self):
		self.get_gate_coordinates = GetCoordinates("blue")
		self.motor_controller = MotorController()

	def turn(self):

		coordinates = self.get_gate_coordinates.get_coordinates()
		while coordinates == -1:
			self.motor_controller.stop()
			self.motor_controller.move_back_wheel(50)

		x = coordinates[0]

		while True:
			if x < 300:
				self.motor_controller.stop()
				self.motor_controller.move_back_wheel(50)
			else:
				break
			'''elif x > 350:
				self.motor_controller.stop()
				self.motor_controller.move_back_wheel(-30)'''


		self.motor_controller.stop()
		self.motor_controller.move_right_wheel(100)
		self.motor_controller.move_left_wheel(100)
		time.sleep(0.5)
		self.motor_controller.stop()

