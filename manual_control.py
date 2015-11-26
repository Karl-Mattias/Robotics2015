from motor_controller import MotorController
from datetime import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((1, 1))
running = True

while running:

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		MotorController().move_back_wheel(10)
		MotorController().move_left_wheel(10)
		MotorController().move_right_wheel(10)

	if keys[pygame.K_RIGHT]:
		MotorController().move_back_wheel(-10)
		MotorController().move_left_wheel(-10)
		MotorController().move_right_wheel(-10)

	if keys[pygame.K_UP]:
		print("sending" + str(datetime.now().time()))
		MotorController().move_right_wheel(20)
		MotorController().move_left_wheel(-20)
		print("back" + str(datetime.now().time()))

	if keys[pygame.K_DOWN]:
		MotorController().move_right_wheel(-20)
		MotorController().move_left_wheel(20)

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.KEYUP:
			MotorController().stop()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
