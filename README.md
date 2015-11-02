# Robotics2015

Activity Log for 2015-09-25
===========================
1. Created the following files
	factory.py ===> We can set global settings for the robot from within this file with pythons pickle module
	settings.py ==> Class file which renders setting and retrieving global settings for bold
	goal_colour_calibrator.py ==> This is the logic file for detecting the goal posts.

Activity Log for 2015-10-09
===========================
1. Created the following files
	motor_controller.py => Class that creates a connection to a given motor and then moves the motor when called with a given speed.
	motor_game.py =======> A simple script to test the motors with arrow keys.
	drive_towards.py ====> Currently just displays what wheel to move. When correctly implemented should use motor_ controller to move towards a given coordinate.
	drive_to_ball.py ====> Uses drive_towards.py and get_ball_coordinates to drive towards the ball.

2. Changed the following files
	get_ball_coordinates.py ==> Now returns the coordinates and size of the biggest ball seen
	simple_colour_calibrator => Generified colour calibrators a bit