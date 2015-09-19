#Convert image to grayscale and display inary thresgholding
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

def threshold(x):
    pass
cv2.namedWindow('frame')
cv2.createTrackbar('s','frame',0,255,threshold)
cv2.createTrackbar('e','frame',0,255,threshold)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    s = cv2.getTrackbarPos('s','frame')
    e = cv2.getTrackbarPos('e','frame')
    threshHolder = cv2.inRange(gray,np.array([s]),np.array([e]))

    # Display the resulting frame
    cv2.imshow('frame',threshHolder)
    px = gray[100,40]

    print px
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
