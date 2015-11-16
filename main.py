from referee import RefereeController
from drive_to_ball import DriveController
from drive_towards import DriveTowards
from game_status import GameStatus
from mainboard_controller import MainBoardController
import threading
import traceback

__author__ = 'Gabriel'

f = open('referee.command', 'w')
f.write("False")
f.close()

referee_controller = RefereeController()
drive_controller = DriveController()
game_status = GameStatus()
drive_towards = DriveTowards()
mainboard_controller = MainBoardController()

initial = True

try:
	td = threading.Thread(target=referee_controller.listen)
	td.start()

	while 1:

		print(game_status.status())

		if game_status.status():
			mainboard_controller.charge()
			mainboard_controller.ping()
			if initial:
				drive_towards.drive_forward()
				initial = False
			drive_controller.drive_to_ball()
		else:
			initial = True

except KeyboardInterrupt:
	referee_controller.kill_received = True
	drive_controller.kill()

except Exception as err:
	traceback.print_exc()
	drive_controller.kill()

