import numpy as np
import cv2

__author__ = 'Karl'


def get_ball_coordinates():

	def nothing(x):
		pass

	cap = cv2.VideoCapture(0)

	cv2.namedWindow('image')

	positions_file = open('Ball_Slider_Positions.txt', 'r')

	kernel = np.ones((10, 10), np.uint8)

	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	h_low = int(positions_file.readline())
	h_top = int(positions_file.readline())
	s_low = int(positions_file.readline())
	s_top = int(positions_file.readline())
	v_low = int(positions_file.readline())
	v_top = int(positions_file.readline())

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

	detector = cv2.SimpleBlobDetector_create(params)

	# Detect blobs.
	keypoints = detector.detect(opening)

	# Getting the blobs coordinates
	coordinates = []
	for elm in keypoints:
		coordinates.append([elm.pt[0], elm.pt[1]])

	return coordinates

print(get_ball_coordinates())
