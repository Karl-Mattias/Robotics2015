import serial


class MotorController:

	def __init__(self):
		self.motor = serial.Serial("COM4", 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)  # , writeTimeout=0)

	# The ids for right, left and back wheel controllers are 1, 2 and 3 respectively
	def move_right_wheel(self, speed=40):
		self.motor.write("1" + ':sd' + str(speed) + '\n')

	def move_left_wheel(self, speed=40):
		self.motor.write("2" + ':sd' + str(speed) + '\n')

	def move_back_wheel(self, speed=40):
		self.motor.write("3" + ':sd' + str(speed) + '\n')

	def stop(self):
		self.motor.write("3" + ':sd' + "0" + '\n')
		self.motor.write("2" + ':sd' + "0" + '\n')
		self.motor.write("1" + ':sd' + "0" + '\n')
