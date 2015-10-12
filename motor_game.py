from motor_controller import MotorController
import pygame

pygame.init()
screen = pygame.display.set_mode((1, 1))
running = True

right_wheel = MotorController(1)
left_wheel = MotorController(2)
back_wheel = MotorController(3)

while running:

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		back_wheel.move(30)
		left_wheel.move(30)

	if keys[pygame.K_RIGHT]:
		right_wheel.move(30)
		back_wheel.move(-30)

	if keys[pygame.K_UP]:
		left_wheel.move(30)
		right_wheel.move(30)

	if keys[pygame.K_DOWN]:
		left_wheel.move(-30)
		right_wheel.move(-30)

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.KEYUP:
			left_wheel.move(0)
			right_wheel.move(0)
			back_wheel.move(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
