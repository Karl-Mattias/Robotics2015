from motor_controller import MotorController

__author__ = 'Karl'


class DriveTowards:

	def __init__(self):
		self.motor_controller = MotorController()

	def drive(self, coordinates):

		if coordinates == -1:
			self.motor_controller.stop()
			return

		x = coordinates[0]
		y = coordinates[1]
		size = coordinates[2]

		if y < 150:
			speed = 50
		else:
			speed = 25

		# the added multiplier to differentiate the wheel speeds
		turning_speed = ((abs(x - 325) / 325) * ((y - 650) / -650)) * speed
		print("turning speed: " + str(turning_speed))

		if x > 325:
			print("move right")
			self.motor_controller.stop()
			self.motor_controller.move_left_wheel((speed + turning_speed) * -1)
			self.motor_controller.move_right_wheel(speed - turning_speed)
		else:
			print("move left")
			self.motor_controller.stop()
			self.motor_controller.move_right_wheel(speed + turning_speed)
			self.motor_controller.move_left_wheel((speed - turning_speed) * -1)
		'''else:
			print("move forwards")
			self.motor_controller.stop()
			self.motor_controller.move_right_wheel(speed)
			self.motor_controller.move_left_wheel(speed * -1)'''