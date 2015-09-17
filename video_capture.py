import numpy as np
import cv2

def nothing(x):
	pass

cap = cv2.VideoCapture(1)


cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low','image',0,255,nothing)
cv2.createTrackbar('H_top','image',0,255,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('S_top','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)
cv2.createTrackbar('V_top','image',0,255,nothing)

file = open('slider_positions.txt', 'r')

cv2.setTrackbarPos('H_low', 'image', int(file.readline()))
cv2.setTrackbarPos('H_top', 'image', int(file.readline()))
cv2.setTrackbarPos('S_low', 'image', int(file.readline()))
cv2.setTrackbarPos('S_top', 'image', int(file.readline()))
cv2.setTrackbarPos('V_low', 'image', int(file.readline()))
cv2.setTrackbarPos('V_top', 'image', int(file.readline()))

kernel = np.ones((5,5),np.uint8)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	'''
	if cv2.waitKey(1) & 0xFF == ord('m'):
		mirrored = cv2.flip(frame, 1)
	elif cv2.waitKey(1) & 0xFF == ord('n'):
		mirrored = cv2.flip(frame, 0)
	elif cv2.waitKey(1) & 0xFF == ord('b'):
		mirrored = cv2.flip(frame, 2)
	else:
		mirrored = frame
	'''

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	H_low = cv2.getTrackbarPos('H_low', 'image')
	H_top = cv2.getTrackbarPos('H_top', 'image')
	S_low = cv2.getTrackbarPos('S_low', 'image')
	S_top = cv2.getTrackbarPos('S_top', 'image')
	V_low = cv2.getTrackbarPos('V_low', 'image')
	V_top = cv2.getTrackbarPos('V_top', 'image')

	# ret, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

	lower_colour = np.array([H_low, S_low, V_low])
	upper_colour = np.array([H_top, S_top, V_top])

	mask = cv2.inRange(hsv, lower_colour, upper_colour)

	# Set up the detector with default parameters.
	params = cv2.SimpleBlobDetector_Params()
	params.blobColor = 255
	params.minThreshold = 40
	params.maxThreshold = 60
	params.thresholdStep = 5

	params.minArea = 100
	params.minConvexity = 0.3
	params.minInertiaRatio = 0.01

	params.maxArea = 20000
	params.maxConvexity = 10

	params.filterByColor = True
	params.filterByCircularity = False

	detector = cv2.SimpleBlobDetector_create(params)

	# Detect blobs.
	keypoints = detector.detect(mask)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	img_with_keypoints = cv2.drawKeypoints(mask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	opening = cv2.morphologyEx(img_with_keypoints, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(img_with_keypoints, cv2.MORPH_CLOSE, kernel)

	# Display the resulting frame
	cv2.imshow('frame', mask)
	cv2.imshow('keypoints', img_with_keypoints)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		file = open("slider_positions.txt", "w")
		file.write(str(H_low) + "\n")
		file.write(str(H_top) + "\n")
		file.write(str(S_low) + "\n")
		file.write(str(S_top) + "\n")
		file.write(str(V_low) + "\n")
		file.write(str(V_top) + "\n")
		file.close()
		break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()