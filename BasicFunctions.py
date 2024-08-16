import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

frameWidth = 270
frameHeight = 270
path = "images/Screenshot (1).png"
img = cv2.imread(path)
img1 = cv2.resize(img, (frameWidth, frameHeight))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.resize(imgGray, (frameWidth, frameHeight))

imgBlur = cv2.GaussianBlur(img, (9, 9), 0)
img3 = cv2.resize(imgBlur, (frameWidth, frameHeight))

imgCanny = cv2.Canny(img, 100, 200)
img4 = cv2.resize(imgCanny, (frameWidth, frameHeight))

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
img5 = cv2.resize(imgDilation, (frameWidth, frameHeight))

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
img6 = cv2.resize(imgEroded, (frameWidth, frameHeight))

cv2.imshow("My Image", img1)  # original image
cv2.imshow("My Gray", img2)  # gray image
cv2.imshow("My Blur", img3)  # blur image
cv2.imshow("My Canny", img4)  # canny image
cv2.imshow("My Dilate", img5)  # dilated image
cv2.imshow("My Erode", img6)  # eroded image
cv2.waitKey(0)