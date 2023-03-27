import cv2
import numpy as np
# 1
image = cv2.imread('-1.jpg')
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]
image_b = np.dstack((b, np.zeros(b.shape, np.uint8), np.zeros(b.shape, np.uint8)))
gray = 0.114 * b + 0.587 * g + 0.299 * r
gray = gray.astype(np.uint8)
cv2.imshow("gray", gray)
cv2.waitKey(0)

