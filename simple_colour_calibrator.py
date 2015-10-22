import numpy as np
from settings import BoltSettings
import cv2

# Load Global Settings
st = BoltSettings()
settingsDict = st.read_dict()
# opg = settingsDict['own_goal_color']
opg = "ball"


# Main Module Begins Here
def nothing(x):
	pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low', 'image', 0, 255, nothing)
cv2.createTrackbar('H_top', 'image', 0, 255, nothing)
cv2.createTrackbar('S_low', 'image', 0, 255, nothing)
cv2.createTrackbar('S_top', 'image', 0, 255, nothing)
cv2.createTrackbar('V_low', 'image', 0, 255, nothing)
cv2.createTrackbar('V_top', 'image', 0, 255, nothing)

# file = open('Blue_Slider_Positions.txt', 'r')

cv2.setTrackbarPos('H_low', 'image', int(settingsDict['H_low_' + opg]))
cv2.setTrackbarPos('H_top', 'image', int(settingsDict['H_top_' + opg]))
cv2.setTrackbarPos('S_low', 'image', int(settingsDict['S_low_' + opg]))
cv2.setTrackbarPos('S_top', 'image', int(settingsDict['S_top_' + opg]))
cv2.setTrackbarPos('V_low', 'image', int(settingsDict['V_low_' + opg]))
cv2.setTrackbarPos('V_top', 'image', int(settingsDict['V_top_' + opg]))

cv2.resizeWindow("image", 600, 300)

kernel = np.ones((10, 10), np.uint8)

while True:
	# Capture frame-by-frame
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	H_low = cv2.getTrackbarPos('H_low', 'image')
	H_top = cv2.getTrackbarPos('H_top', 'image')
	S_low = cv2.getTrackbarPos('S_low', 'image')
	S_top = cv2.getTrackbarPos('S_top', 'image')
	V_low = cv2.getTrackbarPos('V_low', 'image')
	V_top = cv2.getTrackbarPos('V_top', 'image')

	lower_colour = np.array([H_low, S_low, V_low])
	upper_colour = np.array([H_top, S_top, V_top])

	mask = cv2.inRange(hsv, lower_colour, upper_colour)

	# making edges of the two different colours to be less fuzzy
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
	'''
	# Set up the detector with parameters.
	params = cv2.SimpleBlobDetector_Params()
	params.blobColor = 255
	params.minThreshold = 40
	params.maxThreshold = 60
	params.thresholdStep = 5

	params.maxArea = 200000
	params.minArea = 100

	params.maxConvexity = 10
	params.minConvexity = 0.3
	params.minInertiaRatio = 0.01

	params.filterByColor = True
	params.filterByCircularity = False

	detector = cv2.SimpleBlobDetector_create(params)
	'''
	# Detect blobs.
	_, contours, _ = cv2.findContours(opening, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	# keypoints = detector.detect(opening)

	# Draw detected blobs as red circles.

	# Display the resulting frame
	# cv2.imshow('frame', mask)
	# cv2.imshow('keypoints', img_with_keypoints)
	# cv2.imshow('opening', opening)

	if contours:
		cnt = contours[0]
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		## print(str(cx) + ", " + str(cy))

		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)
		cv2.circle(frame, center, radius, (0, 255, 0), 2)

	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		file = open("Slider_Positions.txt", "w")
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
