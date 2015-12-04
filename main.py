from referee import RefereeController
from drive_to_ball import DriveToBall
from drive_controller import DriveController
from mainboard_controller import MainBoardController
from motor_controller import MotorController
import threading

__author__ = 'Gabriel'

referee_controller = RefereeController(game_status=False)
mainboard_controller = MainBoardController()
motor_controller = MotorController()
drive_controller = DriveController(mainboard_controller, motor_controller)
drive_to_ball = DriveToBall(mainboard_controller, drive_controller, referee_controller)

initial = True

try:
	td1 = threading.Thread(target=referee_controller.listen)
	td2 = threading.Thread(target=mainboard_controller.read_from_port)
	td1.start()
	td2.start()

	print("listening ...")

	while True:

		if referee_controller.game_status():
			mainboard_controller.ping()
			mainboard_controller.start_dribbler()
			mainboard_controller.charge()
			print("received go signal")
			if initial:
				drive_controller.drive_forward()
				initial = False
			drive_to_ball.drive_to_ball()

except KeyboardInterrupt:
	referee_controller.kill_received = True

