import cv2

frameWidth, frameHeight = 540, 300

path = "images/Screenshot (1).png"
img = cv2.imread(path)
imgResize = cv2.resize(img, (frameWidth, frameHeight))
print(imgResize.shape)

imgCropped = img[300:540, 430:480]  # height, width
cv2.imshow("soul cropped", imgCropped)
cv2.imshow("soul", imgResize)
cv2.waitKey(0)