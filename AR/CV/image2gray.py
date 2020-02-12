# ---------------------------------------------------- # 

## Image Gray Scale
import numpy as np
import cv2

img = cv2.imread("assets/foto_carlos.jpg", 0)
cv2.imshow('Carlos', img)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to quit all windows
    cv2.destroyAllWindows()

elif k == ord('s'):
    # Wait for S key to save and exit
    cv2.imwrite("assets/carlos_gray.jpg", img)
    cv2.destroyAllWindows()