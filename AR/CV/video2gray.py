# ---------------------------------------------------- # 

import numpy as np
import cv2

# Capture from webcam
cap = cv2.VideoCapture(0)

# Open video file
# cap = cv2.VideoCapture("test.avi")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame
    cv2.imshow('Video Frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()