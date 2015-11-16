import os
import serial

__author__ = 'Karl'


class MainBoardController:

	def __init__(self):
		os.chmod("/dev/tty", 755)  # set permissions to read serial
		self.mainboard = serial.Serial("/dev/tty", 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 3)

	def ping(self):
		self.mainboard.write("p")

	def start_dribbler(self):
		self.mainboard.write("dm50")

	def stop_dribbler(self):
		self.mainboard.write("dm0")

	def charge(self):
		self.mainboard.write("co1")

	def kick(self):
		self.mainboard.write("k")
		self.charge()

	def has_ball(self):
		self.mainboard.write("bl")
		line = self.mainboard.readline()
		print("read from serial: " + line)
		if line == "<bl:1>":
			return True
		else:
			return False
