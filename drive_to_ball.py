from get_coordinates import GetCoordinates
from drive_towards import DriveTowards
from turn_to_goal import TurnToGoal
from game_status import GameStatus

__author__ = 'Karl'


class DriveController(object):

    def __init__(self):
        self.get_ball_coordinates = GetCoordinates("ball")
        self.driver = DriveTowards()
        self.to_goal = TurnToGoal()
        self.i = 0
        self.game_status = GameStatus()

    def drive_to_ball(self):

        while self.game_status.status():
            coordinates = self.get_ball_coordinates.get_coordinates()
            self.driver.drive(coordinates)
            self.i += 1
            if coordinates != -1:
                self.i = 0
                print("Y:", coordinates[1])
                if coordinates[1] > 450:
                    print("near ball")
                    self.to_goal.turn()
                    break
            else:
                if self.i > 10:
                    self.driver.circle()

    def kill(self):
        self.get_ball_coordinates.kill()
