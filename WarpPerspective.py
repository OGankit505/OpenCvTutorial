import cv2
import numpy as np

img = cv2.imread("images/img.png")
width, height = 1000, 750
pts1 = np.float32([[197, 345], [605, 149], [389, 582], [818, 346]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
   cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("original", img)
cv2.imshow("output", output)
cv2.waitKey(0)