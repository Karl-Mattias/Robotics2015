from motor_controller import MotorController
from time import sleep
import pygame

'''
while True:
	MotorController(255).move(50)
	sleep(3)
	MotorController(255).move(-50)
	sleep(3)'''

pygame.init()
screen = pygame.display.set_mode((1, 1))
running = True

while running:

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		MotorController(255).move(50)

	if keys[pygame.K_RIGHT]:
		MotorController(255).move(-50)

	if keys[pygame.K_UP]:
		MotorController(255).move(100)

	if keys[pygame.K_DOWN]:
		MotorController(255).move(-100)

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.KEYUP:
			MotorController(255).move(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
