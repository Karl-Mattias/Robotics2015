from motor_controller import MotorController
import pygame

pygame.init()
screen = pygame.display.set_mode((1, 1))
running = True
up = 0
down = 0
left = 0
right = 0
state = {'up': 0, 'down': 0, 'left': 0, 'right': 0}

while True:
	elist = pygame.event.get()
	for event in elist:
		if event.type == 2 and event.dict.get('key') == 27:
			MotorController().stop()
			quit()
		if event.type == 2:
			if event.dict.get('key') == 273:
				state['up'] = 1
			elif event.dict.get('key') == 274:
				state['down'] = 1
			elif event.dict.get('key') == 275:
				state['right'] = 1
			elif event.dict.get('key') == 276:
				state['left'] = 1
		if event.type == 3:
			if event.dict.get('key') == 273:
				state['up'] = 0
			elif event.dict.get('key') == 274:
				state['down'] = 0
			elif event.dict.get('key') == 275:
				state['right'] = 0
			elif event.dict.get('key') == 276:
				state['left'] = 0
	if state['up'] == 1:
		if state['right'] == 1:
			MotorController().move_left_wheel(-30)
			MotorController().move_right_wheel(30)
			MotorController().move_back_wheel(10)
		elif state['left'] == 1:
			MotorController().move_left_wheel(-30)
			MotorController().move_right_wheel(30)
			MotorController().move_back_wheel(-10)
		else:
			MotorController().move_left_wheel(-40)
			MotorController().move_right_wheel(40)
	elif state['left'] == 1:
		MotorController().move_back_wheel(-20)
		MotorController().move_right_wheel(-20)
		MotorController().move_left_wheel(-20)
	elif state['right'] == 1:
		MotorController().move_back_wheel(20)
		MotorController().move_right_wheel(20)
		MotorController().move_left_wheel(20)
	elif state['down'] == 1:
		MotorController().move_right_wheel(-20)
		MotorController().move_left_wheel(20)
	else:
		MotorController().stop()

	'''keys = pygame.key.get_pressed()
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
				running = False'''
