
import cv2 
import numpy as np

img = cv2.imread("assets/lena_noise.jpg", 0)
out = np.zeros((img.shape))

rows = len(img)
columns = len(img[0])

for i in range(0, rows):
    for j in range (0, columns):
            out[i][j] = img[i][j]

img2 = np.zeros(shape = (rows + 1, columns + 1))

for i in range(0, rows + 1):
    for j in range (0, columns + 1):
        if i != 0 & j != 0:
            img2[i][j] = img[i][j]
        
cv2.imwrite("assets/lena_unnoise.jpg", out)
cv2.imshow("assets/lena_unnoise.jpg", out)

# rows = len(img2)
# columns = len(img2[0])

# kernel = np.zeros(9)
# for i in range (0, 9):
#     kernel[i] = 1/9
# kernel = kernel.reshape((3,3))

# for i in range(1, rows - 1):
#     for j in range (1, columns - 1):
#         mid = 0
#         for x in range (0, 3):
#             for y in range (0, 3):
#                 mid += img[x, y] 
#         out[i][j]

# cv2.imwrite("assets/lena_unnoise.jpg", out)
# cv2.imshow("assets/lena_unnoise.jpg", out)
k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to quit all windows
    cv2.destroyAllWindows()
