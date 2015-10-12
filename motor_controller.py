import serial


class MotorController:

	def __init__(self, controller_id):
		port = "COM9"
		self.motor = serial.Serial(port, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 3)
		self.controller_id = controller_id
		#self.motor_id = motor_id

	def move(self, speed=40):
		self.motor.write(str(self.controller_id) + ':sd' + str(speed) + '\n')
		#data = self.motor.read(9999)
