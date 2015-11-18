import os
import serial

__author__ = 'Karl'


class MainBoardController:

	def __init__(self):
		os.chmod("/dev/ttyACM1", 755)  # set permissions to read serial
		self.mainboard = serial.Serial("/dev/ttyACM1", 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 3)

	def ping(self):
		self.mainboard.write("p\n")

	def start_dribbler(self):
		self.mainboard.write("dm50\n")

	def stop_dribbler(self):
		self.mainboard.write("dm0\n")

	def charge(self):
		self.mainboard.write("co1\n")

	def kick(self):
		self.mainboard.write("k\n")
		self.charge()

	def has_ball(self):
		return self.is_ball

	def read_from_port(self):
		self.is_ball = False
		while True:
			line = self.mainboard.readline().strip()
			print("read from serial: " + line)
			print(line+"==<bl:1>")
			'''if "1" in line:
				return True'''
			if line == "<bl:1>":
				self.is_ball = True
			if line == "<bl:0>":
				self.is_ball = False
