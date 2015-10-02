import serial


class MotorController:

	def __init__(self, motor_id):
		self.motor = serial.Serial('COM5', 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
		self.motor_id = motor_id

	def move(self, speed=40):
		self.motor.write('sd' + str(speed) + '\n')
		#data = self.motor.read(9999)
		#print(data)
