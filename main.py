from referee import RefereeController
from drive_to_ball import DriveController
import threading

__author__ = 'Gabriel'

td = threading.Thread(target=RefereeController.listen)
td.start()

while 1:
    f = open('referee.command','r')
    play_on = eval(f.readline())

    if (play_on == True):
        DriveController.drive_to_ball()

