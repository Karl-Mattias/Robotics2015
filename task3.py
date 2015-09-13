#Convert image to grayscale and display inary thresgholding
import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (retval, threshHolder) = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow('frame',threshHolder)
    px = gray[100,40]

    print px
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
