from motor_controller import MotorController
import time

__author__ = 'Karl'


class DriveTowards:

	def __init__(self):
		self.motor_controller = MotorController()

	def drive(self, coordinates):

		if coordinates == -1:
			#self.motor_controller.stop()
			return

		x = coordinates[0]
		y = coordinates[1]
		# size = coordinates[2]

		if y < 150:
			speed = 40
		else:
			speed = 30

		# the added multiplier to differentiate the wheel speeds.
		# the smaller the y value the least is needed to turn, because the farthest is the ball.
		# the closer the x value is to the central value (325) the least is needed to turn.
		turning_speed = ((abs(x - 325) / 325.0) * ((650 - y) / 650.0)) * speed
		print("turning speed: " + str(turning_speed))

		if x > 325:
			print("move right")
			#self.motor_controller.stop()
			self.motor_controller.move_left_wheel((speed + turning_speed) * -1)
			self.motor_controller.move_right_wheel(speed - turning_speed)
		else:
			print("move left")
			#self.motor_controller.stop()
			self.motor_controller.move_right_wheel(speed + turning_speed)
			self.motor_controller.move_left_wheel((speed - turning_speed) * -1)

	def circle(self):
		self.motor_controller.move_left_wheel(10)
		self.motor_controller.move_right_wheel(10)
		self.motor_controller.move_back_wheel(10)

	def drive_forward(self):
		self.motor_controller.move_left_wheel(-70)
		self.motor_controller.move_right_wheel(70)
		time.sleep(1.5)
