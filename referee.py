import serial
from settings import BoltSettings

__author__ = 'Gabriel'


class RefereeController(object):
	def __init__(self):
		self.serialChannel = serial.Serial("/dev/ttyACM0", 9600)
		self.boltSettings = BoltSettings().read_dict()
		self.CharCounter = 0
		self.initChar = self.boltSettings['initialCharSignal']
		self.listening = False
		self.respond = False
		self.kill_received = False

	def write_ack_string(self):

		print("playingField: " + self.initChar + self.boltSettings["playingField"] + self.boltSettings["robotID"] + self.boltSettings["ackMsg"])
		print("intChar: " + (self.initChar + self.boltSettings["playingField"] + self.boltSettings["robotID"] + self.boltSettings["ackMsg"]).encode())
		message = (self.initChar + self.boltSettings["playingField"] + self.boltSettings["robotID"] + self.boltSettings["ackMsg"]).encode()
		print("message: " + message)
		self.serialChannel.write(message)

	def write_last_ctr_signal(self, msg):
		f = open('referee.command', 'w')
		f.write(msg)
		f.close()

	def listen(self):
		while not self.kill_received:
			self.CharCounter += 1
			char_signal = self.serialChannel.read().decode()
			print(char_signal)
			if char_signal == self.initChar:
				self.CharCounter = 0
				self.listening = True
				continue
			if not self.listening:
				continue  # wait for next a
			if self.CharCounter == 1 and char_signal != self.boltSettings['playingField']:
				self.listening = False
			if self.CharCounter == 2 and char_signal != self.boltSettings['robotID'] and char_signal != self.boltSettings['allRobotsChar']:
				self.listening = False
			if self.CharCounter == 2 and char_signal == self.boltSettings['robotID']:
				self.respond = True
			if self.CharCounter == 2 and char_signal == self.boltSettings['allRobotsChar']:
				self.respond = False
			if self.CharCounter == 2 and self.listening:
				msg = ""
				for self.CharCounter in range(3, 12):
					char_signal = self.serialChannel.read().decode()
					print(char_signal)
					if char_signal == self.initChar:
						self.CharCounter = 0
						break
					if char_signal == "-":
						self.listening = False
						break
					msg += char_signal
					if msg in ["START", "STOP"]:
						print(msg)
						if self.respond:
							self.write_ack_string()

						if msg == "START":
							self.write_last_ctr_signal('True')
						else:
							self.write_last_ctr_signal('False')
