from referee import RefereeController
from drive_to_ball import DriveController
from drive_towards import DriveTowards
from mainboard_controller import MainBoardController
from motor_controller import MotorController
import threading
import traceback

__author__ = 'Gabriel'

f = open('referee.command', 'w')
f.write("True")
f.close()

referee_controller = RefereeController(game_status=True)
mainboard_controller = MainBoardController()
motor_controller = MotorController()
drive_controller = DriveController(mainboard_controller, motor_controller, referee_controller)
drive_towards = DriveTowards(mainboard_controller, motor_controller)

initial = True

try:
	#td1 = threading.Thread(target=referee_controller.listen)
	td2 = threading.Thread(target=mainboard_controller.read_from_port)
	#td1.start()
	td2.start()

	print("listening ...")

	while True:

		if referee_controller.game_status():
			mainboard_controller.ping()
			mainboard_controller.start_dribbler()
			mainboard_controller.charge()
			print("received go signal")
			if initial:
				# drive_towards.drive_forward()
				initial = False
			drive_controller.drive_to_ball()

except KeyboardInterrupt:
	referee_controller.kill_received = True
	# drive_controller.kill()

except Exception as err:
	traceback.print_exc()
	# drive_controller.kill()

