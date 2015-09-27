import numpy as np
from settings import BoltSettings
import cv2
import sys

#Load Global Settings
st = BoltSettings()
settingsDict = st.readDict()
opg = settingsDict['opponent_goal_color'] #Getting the opponents goal post color

#Main Module Begins Here
def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low','image',0,255,nothing)
cv2.createTrackbar('H_top','image',0,255,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('S_top','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)
cv2.createTrackbar('V_top','image',0,255,nothing)

#file = open('Ball_Slider_Positions.txt', 'r')

cv2.setTrackbarPos('H_low', 'image', int(settingsDict['H_low_'+opg]))
cv2.setTrackbarPos('H_top', 'image', int(settingsDict['H_top_'+opg]))
cv2.setTrackbarPos('S_low', 'image', int(settingsDict['S_low_'+opg]))
cv2.setTrackbarPos('S_top', 'image', int(settingsDict['S_top_'+opg]))
cv2.setTrackbarPos('V_low', 'image', int(settingsDict['V_low_'+opg]))
cv2.setTrackbarPos('V_top', 'image', int(settingsDict['V_top_'+opg]))

kernel = np.ones((10, 10), np.uint8)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray_img,127,255,0)
	img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print len(approx)
		if len(approx)==5:
			print "pentagon"
			cv2.drawContours(img,[cnt],0,255,-1)
		elif len(approx)==3:
			print "triangle"
			cv2.drawContours(img,[cnt],0,(0,255,0),-1)
		elif len(approx)==4:
			print "square"
			cv2.drawContours(img,[cnt],0,(0,0,255),-1)
		elif len(approx) == 9:
			print "half-circle"
			cv2.drawContours(img,[cnt],0,(255,255,0),-1)
		elif len(approx) > 15:
			print "circle"
			cv2.drawContours(img,[cnt],0,(0,255,255),-1)

	#cnt = contours[4]
	#img = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	#img_with_keypoints = cv2.drawKeypoints(opening, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	# Display the resulting frame
	cv2.imshow('Video', img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		'''
		file = open("Ball_Slider_Positions.txt", "w")
		file.write(str(H_low) + "\n")
		file.write(str(H_top) + "\n")
		file.write(str(S_low) + "\n")
		file.write(str(S_top) + "\n")
		file.write(str(V_low) + "\n")
		file.write(str(V_top) + "\n")
		file.close()
		'''
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
