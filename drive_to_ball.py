from get_coordinates import GetCoordinates
from drive_towards import DriveTowards
from turn_to_goal import TurnToGoal

__author__ = 'Karl'

class DriveController(object):

    def drive_to_ball(self):
        get_ball_coordinates = GetCoordinates("ball")
        driver = DriveTowards()
        to_goal = TurnToGoal()
        i = 0

        while True:
            coordinates = get_ball_coordinates.get_coordinates()
            driver.drive(coordinates)
            i += 1
            if coordinates != -1:
                i = 0
                print("Y:", coordinates[1])
                if coordinates[1] > 450:
                    print("near ball")
                    to_goal.turn()
                    break
            else:
                if i > 10:
                    driver.circle()


#drive_to_ball()
