import numpy as np
import cv2
from settings import BoltSettings

__author__ = 'Karl'

# Load Global Settings
st = BoltSettings()
settingsDict = st.read_dict()


def get_ball_coordinates():

	cap = cv2.VideoCapture(1)

	kernel = np.ones((10, 10), np.uint8)

	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	h_low = int(settingsDict['H_low_ball'])
	h_top = int(settingsDict['H_top_ball'])
	s_low = int(settingsDict['S_low_ball'])
	s_top = int(settingsDict['S_top_ball'])
	v_low = int(settingsDict['V_low_ball'])
	v_top = int(settingsDict['V_top_ball'])

	lower_colour = np.array([h_low, s_low, v_low])
	upper_colour = np.array([h_top, s_top, v_top])

	mask = cv2.inRange(hsv, lower_colour, upper_colour)

	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

	# Set up the detector with parameters.
	params = cv2.SimpleBlobDetector_Params()
	params.blobColor = 255
	params.minThreshold = 40
	params.maxThreshold = 60
	params.thresholdStep = 5

	params.maxArea = 20000
	params.minArea = 100

	params.maxConvexity = 10
	params.minConvexity = 0.3
	params.minInertiaRatio = 0.01

	params.filterByColor = True
	params.filterByCircularity = False

	detector = cv2.SimpleBlobDetector(params)

	# Detect blobs.
	keypoints = detector.detect(opening)

	# Getting the biggest blobs coordinates (that is the closest object)
	biggest_size = 0
	coordinates = -1
	for elm in keypoints:
		if elm.size > biggest_size:
			biggest_size = elm.size
			coordinates = (elm.pt[0], elm.pt[1], biggest_size)

	return coordinates
