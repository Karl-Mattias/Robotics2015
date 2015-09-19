__author__ = 'gabriel'

import cv2
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 1
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#outFile = cv2.VideoWriter('gabby_playback.avi',fourcc, 20.0, (640,480))
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()

print("Taking image...")
# Take the actual image we want to keep

while cv2.waitKey(1)!= 27:
    camera_capture = get_image()
    # correct format based on the file extension you provide. Convenient!
    cv2.imshow("gabby", camera_capture)
    #outFile.write(camera_capture)


 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)