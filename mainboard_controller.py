import os
import serial

__author__ = 'Karl'


class MainBoardController:

	def __init__(self):
		os.chmod("/dev/ttyACM1", 755)  # set permissions to read serial
		self.mainboard = serial.Serial("/dev/ttyACM1", 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 3)
		self.has_ball = False

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
		return self.has_ball

	def read_from_port(self):
		while True:
			line = self.mainboard.readline().strip()
			print("read from serial: " + line)
			print(line+"==<bl:1>")
			'''if "1" in line:
				return True'''
			if line == "<bl:1>":
				self.has_ball = True
			if line == "<bl:0>":
				self.has_ball = False
