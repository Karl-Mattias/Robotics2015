from referee import RefereeController
from drive_to_ball import DriveController
import threading

__author__ = 'Gabriel'

referee_controller = RefereeController()
td = threading.Thread(target=referee_controller.listen)
td.start()
drive_controller = DriveController()

while 1:
    f = open('referee.command', 'r')
    line = f.readline()
    print(line)
    play_on = eval(line)
    f.close()

    if play_on:
        drive_controller.drive_to_ball()

