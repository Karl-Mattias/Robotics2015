from motor_controller import MotorController
import manual_control

manual_control.init()
screen = manual_control.display.set_mode((1, 1))
running = True

right_wheel = MotorController(1)
left_wheel = MotorController(2)
back_wheel = MotorController(3)

while running:

	keys=manual_control.key.get_pressed()
	if keys[manual_control.K_LEFT]:
		back_wheel.move(30)
		left_wheel.move(30)

	if keys[manual_control.K_RIGHT]:
		right_wheel.move(30)
		back_wheel.move(-30)

	if keys[manual_control.K_UP]:
		left_wheel.move(30)
		right_wheel.move(30)

	if keys[manual_control.K_DOWN]:
		left_wheel.move(-30)
		right_wheel.move(-30)

	events = manual_control.event.get()

	for event in events:
		if event.type == manual_control.KEYUP:
			left_wheel.move(0)
			right_wheel.move(0)
			back_wheel.move(0)
		elif event.type == manual_control.KEYDOWN:
			if event.key == manual_control.K_ESCAPE:
				running = False
