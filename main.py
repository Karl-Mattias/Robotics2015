from referee import RefereeController
from drive_to_ball import DriveController
import threading, time

__author__ = 'Gabriel'

f = open('referee.command', 'w')
f.write("False")
f.close()

referee_controller = RefereeController()
drive_controller = DriveController()
try:
	td = threading.Thread(target=referee_controller.listen)
	td.start()

	while 1:
		f = open('referee.command', 'r')
		line = f.readline()
		print("parse: " + line)
		play_on = eval(line)
		f.close()

		if play_on:
			drive_controller.drive_to_ball()

		time.sleep(1)
except KeyboardInterrupt:
	referee_controller.kill_received = True
	drive_controller.kill()

except:
	drive_controller.kill()

