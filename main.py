from referee import RefereeController
from drive_to_ball import DriveController
from game_status import GameStatus

import threading, time

__author__ = 'Gabriel'

f = open('referee.command', 'w')
f.write("False")
f.close()

referee_controller = RefereeController()
td = threading.Thread(target=referee_controller.listen)
td.start()
drive_controller = DriveController()


while 1:
    f = open('referee.command', 'r')
    line = f.readline()
    print("parse: " + line)
    play_on = eval(line)
    f.close()

    if play_on:
        drive_controller.drive_to_ball()

    time.sleep(1)

