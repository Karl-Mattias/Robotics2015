__author__ = 'gabriel'


import numpy as np
import cv2

ball = cv2.VideoCapture(1)


def threshold(x):
    pass



cv2.namedWindow('frame')
cv2.createTrackbar('g','frame',0,255,threshold)
cv2.createTrackbar('a','frame',0,255,threshold)
cv2.createTrackbar('b','frame',0,255,threshold)
cv2.createTrackbar('r','frame',0,255,threshold)
cv2.createTrackbar('i','frame',0,255,threshold)
cv2.createTrackbar('e','frame',0,255,threshold)




while(True):
    #Each frame we get from the camera
    _, frame = ball.read()

    #convert BGDR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    g=cv2.getTrackbarPos('g','trackbar')
    a=cv2.getTrackbarPos('a','trackbar')
    b=cv2.getTrackbarPos('b','trackbar')
    r=cv2.getTrackbarPos('r','trackbar')
    i=cv2.getTrackbarPos('i','trackbar')
    e=cv2.getTrackbarPos('e','trackbar')

     # Threshold the HSV image to get only the target color from the trackbar which will be orange
    mask = cv2.inRange(hsv,np.array([g,a,b]),np.array([r,i,e]))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #Display
    cv2.imshow('frame',frame)
    cv2.imshow('maskedObject',mask)
    #cv2.imshow('result',res)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()