import cv2
img = cv2.imread("road2.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("road2gray.png",img_gray)

