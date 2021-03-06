import time

__author__ = 'Karl'


class DriveController:

	def __init__(self, mainboard_controller, motor_controller):
		self.motor_controller = motor_controller
		self.mainboard_controller = mainboard_controller

	def drive(self, coordinates):

		if coordinates == -1:
			return

		x = coordinates[0]
		y = coordinates[1]

		# the closer the ball the smaller the speed
		if y < 150:
			speed = 70
		elif y > 500:
			speed = 20
		else:
			speed = 40

		if x > 340:
			# print("move right")
			self.motor_controller.move_left_wheel((speed + 8) * -1)
			self.motor_controller.move_right_wheel(speed - 8)
			self.motor_controller.move_back_wheel(8)
		elif x < 310:
			# print("move left")
			self.motor_controller.move_right_wheel(speed + 8)
			self.motor_controller.move_left_wheel((speed - 8) * -1)
			self.motor_controller.move_back_wheel(8)
		else:
			# print("move straght")
			self.motor_controller.move_right_wheel(speed + 20)
			self.motor_controller.move_left_wheel((speed + 20) * -1)

	def circle(self, multiplier=1):
		self.motor_controller.move_left_wheel(14 * multiplier)
		self.motor_controller.move_right_wheel(14 * multiplier)
		self.motor_controller.move_back_wheel(14 * multiplier)

	def around_ball(self, multiplier=1):
		self.motor_controller.move_back_wheel(10 * multiplier)

	def drive_forward(self):
		self.motor_controller.move_left_wheel(-70)
		self.motor_controller.move_right_wheel(70)
		time.sleep(1)
		self.mainboard_controller.ping()
		time.sleep(1)
		self.mainboard_controller.ping()

	def stop(self):
		self.motor_controller.stop()
