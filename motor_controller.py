import serial


class MotorController:

	def __init__(self, port):
		self.motor = serial.Serial(port, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
		#self.motor_id = motor_id

	def move(self, speed=40):
		self.motor.write('sd' + str(speed) + '\n')
		#data = self.motor.read(9999)
