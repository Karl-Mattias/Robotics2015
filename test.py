from motor_controller import MotorController
from get_coordinates import GetCoordinates

__author__ = 'Karl'

'''motor_controller = MotorController()

motor_controller.move_back_wheel(30)
motor_controller.move_left_wheel(30)
motor_controller.move_right_wheel(30)'''

get_coordinates = GetCoordinates("ball")
coordinates = get_coordinates.get_coordinates()
print(coordinates[1])
