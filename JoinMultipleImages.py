import cv2
import numpy as np

path1 = "images/sign.jpg"
path2 = "images/IMG_3598.jpg"
frameWidth = 512
frameHeight = 512
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img1 = cv2.resize(img1, (frameWidth, frameHeight))
img2 = cv2.resize(img2, (frameWidth, frameHeight))
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

horizontal = np.hstack((img1, img2))
vertical = np.vstack((img1, img2))

cv2.imshow("vertical", vertical)
cv2.imshow("horizontal", horizontal)
cv2.waitKey(0)