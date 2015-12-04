import numpy as np
import cv2
from settings import BoltSettings

__author__ = 'Karl'


class GetCoordinates:

	def __init__(self):
		pass

	@staticmethod
	def get_coordinates():

		# Load Global Settings
		st = BoltSettings()
		settings_dict = st.read_dict()

		cap = cv2.VideoCapture(0)

		ret, frame = cap.read()

		if not ret:
			print("No image")
			print(frame)
			return -1

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		colours = ["black", "blue", "yellow", "ball"]
		coordinates_dict = {"ball": -1, "blue": -1, "yellow": -1, "black": -1}

		for i in range(4):
			colour = colours[i]
			h_low = int(settings_dict['H_low_' + colour])
			h_top = int(settings_dict['H_top_' + colour])
			s_low = int(settings_dict['S_low_' + colour])
			s_top = int(settings_dict['S_top_' + colour])
			v_low = int(settings_dict['V_low_' + colour])
			v_top = int(settings_dict['V_top_' + colour])

			lower_colour = np.array([h_low, s_low, v_low])
			upper_colour = np.array([h_top, s_top, v_top])
			mask = cv2.inRange(hsv, lower_colour, upper_colour)

			kernel = np.ones((10, 10), np.uint8)

			# combining smaller blobs
			dilated = cv2.dilate(mask, kernel, iterations=2)

			# Detect blobs.
			_, contours, _ = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

			# Getting the biggest blob's coordinates (that is probably the closest object)
			biggest_width = 0
			coordinates = -1
			for cnt in contours:
				# width = cv2.contourArea(cnt)
				rect = cv2.minAreaRect(cnt)
				width = rect[1][0]
				height = rect[1][1]

				if width < 5 and (colour == "yellow" or colour == "blue"):
					continue

				if width > biggest_width:
					moment = cv2.moments(cnt)
					try:
						cx = int(moment['m10']/moment['m00'])
						cy = int(moment['m01']/moment['m00'])
					except ZeroDivisionError:
						print("zero division")
						continue
					biggest_width = width
					if colour == "ball":
						black = coordinates_dict["black"]
						# print("black: " + str(black))
						# print("ball: " + str(cx) + ", " + str(cy))
						if black != -1:
							black_x = black[0]
							black_y = black[1]
							black_width = black[2]
							if black_y > cy and black_x + black_width / 2 > cx > black_width / 2 - black_x:  # ball is out of the field
								print("ball out of field")
								continue

					coordinates = (cx, cy, width, height)
			coordinates_dict[colour] = coordinates

		cap.release()

		return coordinates_dict
