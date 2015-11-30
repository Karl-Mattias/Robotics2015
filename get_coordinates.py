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
		colours = ["ball", "blue", "yellow", "black"]
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



			# making edges of the two different colours to be less fuzzy
			closing = cv2.dilate(mask, kernel, iterations=2)
			#closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
			# opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

			# Detect blobs.
			_, contours, _ = cv2.findContours(closing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

			# Getting the biggest blob's coordinates (that is probably the closest object)
			biggest_size = 0
			coordinates = -1
			for cnt in contours:
				area = cv2.contourArea(cnt)
				rect = cv2.minAreaRect(cnt)
				width = rect[1][0]

				if width < 5 and (colour == "yellow" or colour == "blue"):
					continue

				if area > biggest_size:
					biggest_size = area
					M = cv2.moments(cnt)
					try:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					except ZeroDivisionError:
						coordinates = -1
						print("zero division")
						continue
					coordinates = (cx, cy, width)
			coordinates_dict[colour] = coordinates

		cap.release()

		return coordinates_dict

	# def kill(self):
		# self.cap.release()
