from motor_controller import MotorController
import pygame

pygame.init()
screen = pygame.display.set_mode((1, 1))
running = True
port = 'COM5'

while running:

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		MotorController(port).move(50)

	if keys[pygame.K_RIGHT]:
		MotorController(port).move(-50)

	if keys[pygame.K_UP]:
		MotorController(port).move(100)

	if keys[pygame.K_DOWN]:
		MotorController(port).move(-100)

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.KEYUP:
			MotorController(port).move(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
