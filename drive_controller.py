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
		# width = coordinates[2]

		speed = 30
		'''if y < 150:
			speed = 70
		else:
			speed = 40'''

		'''# the added multiplier to differentiate the wheel speeds.
		# the smaller the y value the least is needed to turn, because the farthest is the ball.
		# the closer the x value is to the central value (325) the least is needed to turn.
		turning_speed = ((abs(x - 325) / 325.0) * ((650 - y) / 650.0)) * speed
		print("turning speed: " + str(turning_speed))'''

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

	def circle(self):
		self.motor_controller.move_left_wheel(14)
		self.motor_controller.move_right_wheel(14)
		self.motor_controller.move_back_wheel(14)

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
