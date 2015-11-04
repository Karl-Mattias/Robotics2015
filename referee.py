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

	def writeAckString(self):
		self.serialChannel.write(str(self.initChar + self.boltSettings.playingField + self.boltSettings.robotID + self.boltSettings.ackMsg).encode)

	def writeLastCtrSignal(self, msg):
		f = open('referee.command', 'w')
		f.write(msg)
		f.close()

	def listen(self):
		while not self.kill_received:
			self.CharCounter += 1
			charSignal = self.serialChannel.read().decode()
			print(charSignal)
			if charSignal == self.initChar:
				self.CharCounter = 0
				self.listening = True
				continue
			if not self.listening:
				continue  # wait for next a
			if self.CharCounter == 1 and charSignal != self.boltSettings['playingField']:
				self.listening = False
			if self.CharCounter == 2 and charSignal != self.boltSettings['robotID'] and charSignal != self.boltSettings['allRobotsChar']:
				self.listening = False
			if self.CharCounter == 2 and charSignal == self.boltSettings['robotID']:
				self.respond = True
			if self.CharCounter == 2 and charSignal == self.boltSettings['allRobotsChar']:
				self.respond = False
			if self.CharCounter == 2 and self.listening:
				msg = ""
				for self.CharCounter in range(3, 12):
					charSignal = self.serialChannel.read().decode()
					print(charSignal)
					if charSignal == self.initChar:
						self.CharCounter = 0
						break
					if charSignal == "-":
						self.listening = False
						break
					msg += charSignal
					if msg in ["START", "STOP"]:
						print(msg)
						if self.respond:
							self.writeAckString()

						if msg == "START":
							self.writeLastCtrSignal('True')
						else:
							self.writeLastCtrSignal('False')
