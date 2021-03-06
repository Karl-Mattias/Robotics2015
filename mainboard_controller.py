import serial
from datetime import datetime
__author__ = 'Karl'


class MainBoardController:

	def __init__(self):
		port = 'COM5'
		self.mainboard = serial.Serial(port, 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 3)
		self.is_ball = False

	def ping(self):
		self.mainboard.write("p\n")

	def start_dribbler(self):
		self.mainboard.write("dm255\n")

	def stop_dribbler(self):
		self.mainboard.write("dm0\n")

	def charge(self):
		print(str(datetime.now()) + " | charge")
		self.mainboard.write("c\n")

	def kick(self):
		print(str(datetime.now()) + " | kick")
		self.mainboard.write("k\n")
		self.charge()

	def has_ball(self):
		return self.is_ball

	def read_from_port(self):
		self.is_ball = False
		while True:
			line = self.mainboard.readline().strip()
			'''if "1" in line:
				return True'''
			if line == "<bl:1>":
				self.is_ball = True
			if line == "<bl:0>":
				self.is_ball = False
