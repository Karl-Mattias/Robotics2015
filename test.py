from motor_controller import MotorController
from get_coordinates import GetCoordinates
from time import sleep
from datetime import datetime

__author__ = 'Karl'

motor_controller = MotorController()
'''
print("sending" + str(datetime.now().time()))
motor_controller.move_left_wheel(10)
motor_controller.move_right_wheel(10)
motor_controller.move_back_wheel(10)
print("back" + str(datetime.now().time()))
sleep(0.2)
motor_controller.move_left_wheel(10)
motor_controller.move_right_wheel(10)
motor_controller.move_back_wheel(10)
sleep(0.2)
motor_controller.move_left_wheel(10)
motor_controller.move_right_wheel(10)
motor_controller.move_back_wheel(10)
sleep(0.2)
motor_controller.move_left_wheel(-40)
motor_controller.move_right_wheel(40)
sleep(0.2)
motor_controller.move_left_wheel(-40)
motor_controller.move_right_wheel(40)
sleep(0.2)
motor_controller.move_left_wheel(-10)
motor_controller.move_right_wheel(-10)
motor_controller.move_back_wheel(-10)
sleep(0.2)
'''
motor_controller.move_left_wheel(-20)
motor_controller.move_right_wheel(-20)
motor_controller.move_back_wheel(-20)


# get_coordinates = GetCoordinates("ball")
# coordinates = get_coordinates.get_coordinates()
# print(coordinates[1])
