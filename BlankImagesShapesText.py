import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
#img[:] = 255, 0, 0

# to draw lines on image
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

# to draw a rectangle shape
cv2.rectangle(img, (225, 100), (450, 200), (0, 0, 255), cv2.FILLED)

# to draw a circular shape
cv2.circle(img, (150, 400), 50, (255, 0, 0), cv2.FILLED)  # FILLED means it fills the shape with the particular color

# to write text on an image
cv2.putText(img, "Drawing shapes", (75, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
