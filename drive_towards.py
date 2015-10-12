from motor_controller import MotorController

__author__ = 'Karl'


class DriveTowards:

	def __init__(self):
		self.motor_controller = MotorController()

	def drive(self, coordinates):

		if coordinates == -1:
			return

		x = coordinates[0]
		y = coordinates[1]
		size = coordinates[2]

		if size < 50:
			speed = 50
		else:
			speed = 100

		if x > 400:
			# print("left wheel forwards")
			# print("back wheel left")
			self.motor_controller.move_left_wheel(speed * -1)
			self.motor_controller.move_back_wheel(speed)
		elif x < 250:
			# print("right wheel forwards")
			# print("back wheel right")
			self.motor_controller.move_right_wheel(speed)
			self.motor_controller.move_back_wheel(speed * -1)
		else:
			# print("left wheel forwards")
			# print("right wheel forwards")
			self.motor_controller.move_right_wheel(speed)
			self.motor_controller.move_left_wheel(speed * -1)
