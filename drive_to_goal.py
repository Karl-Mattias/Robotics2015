__author__ = 'Karl'


def drive_to_goal(get_coordinates, drive_controller, mainboard_controller):

	print("objective lost")
	i = 0
	last_state = "circle"

	while i < 10:
		mainboard_controller.ping()

		blue_coordinates = get_coordinates.get_coordinates()["blue"]
		yellow_coordinates = get_coordinates.get_coordinates()["yellow"]

		if blue_coordinates != -1 and blue_coordinates[2] < 300:
			if last_state == "circle":
				drive_controller.stop()

			drive_controller.drive(blue_coordinates)
			last_state = "driving"
		elif yellow_coordinates != -1 and yellow_coordinates[2] < 300:
			if last_state == "circle":
				drive_controller.stop()

			drive_controller.drive(yellow_coordinates)
			last_state = "driving"

		else:
			if last_state == "driving":
				drive_controller.stop()
			drive_controller.circle(2)
			last_state = "circle"

		i += 1
