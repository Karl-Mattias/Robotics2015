import numpy as np
import cv2
from settings import BoltSettings

__author__ = 'Karl'


class GetCoordinates:

	def __init__(self):
		pass

	@staticmethod
	def get_coordinates(obj):

		# Load Global Settings
		st = BoltSettings()
		obj = obj
		settings_dict = st.read_dict()
		h_low = int(settings_dict['H_low_' + obj])
		h_top = int(settings_dict['H_top_' + obj])
		s_low = int(settings_dict['S_low_' + obj])
		s_top = int(settings_dict['S_top_' + obj])
		v_low = int(settings_dict['V_low_' + obj])
		v_top = int(settings_dict['V_top_' + obj])

		lower_colour = np.array([h_low, s_low, v_low])
		upper_colour = np.array([h_top, s_top, v_top])

		cap = cv2.VideoCapture(0)

		kernel = np.ones((10, 10), np.uint8)

		ret, frame = cap.read()

		if not ret:
			print("No image")
			print(frame)
			return -1

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		mask = cv2.inRange(hsv, lower_colour, upper_colour)

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

			if width < 5 and (obj == "yellow" or obj == "blue"):
				return -1

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

		cap.release()

		return coordinates

	def kill(self):
		self.cap.release()
