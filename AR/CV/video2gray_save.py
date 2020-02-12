# ---------------------------------------------------- # 

import numpy as np
import cv2

# Capture from webcam
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("assets/videogray.avi", fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True :

        # Traspass the frame to gray
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the frame
        out.write(frame)

        cv2.imshow('Video Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()