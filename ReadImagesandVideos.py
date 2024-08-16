import cv2

# for image reading
# img = cv2.imread("images/sign.jpg")
# cv2.imshow("My Sign",img)
# cv2.waitKey(0)

frameWidth = 960
frameHeight = 540

# for video reading
# cap = cv2.VideoCapture("images/720p Manjummel Boys (2024) ORG. Hindi Full Movie HD ESub Download.mkv")
# while True:
#     success,img = cap.read()
#     cv2.imshow("Movie", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# for webcam reading
cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
