from motor_controller import MotorController

__author__ = 'Karl'


class DriveTowards:
	'''
	def __init__(self):
		self.right_wheel = MotorController("COM5")
		self.left_wheel = MotorController("COM5")
		self.back_wheel = MotorController("COM5")
	'''
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
			print("left wheel forwards")
			print("back wheel left")
			# self.left_wheel.move(speed)
			# self.back_wheel.move(speed * -1)
		elif x < 250:
			print("right wheel forwards")
			print("back wheel right")
			# self.right_wheel.move(speed)
			# self.back_wheel.move(speed)
		else:
			print("left wheel forwards")
			print("right wheel forwards")
			# self.right_wheel.move(speed)
			# self.left_wheel.move(speed)