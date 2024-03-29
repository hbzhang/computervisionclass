import cv2

import matplotlib.pyplot as plt
nemo = cv2.imread('image.png')
cv2.imshow("BGR", nemo)
cv2.waitKey(0)
cv2.destroyAllWindows()
nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", nemo)
cv2.waitKey(0)
cv2.destroyAllWindows()
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
cv2.imshow("HSV", hsv_nemo)
cv2.waitKey(0)
cv2.destroyAllWindows()
light_orange = (1, 190, 200)
dark_orange = (180, 255, 255)
mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
cv2.imshow("A mask between light and dark orange", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
result = cv2.bitwise_and(nemo, nemo, mask=mask)
cv2.imshow("RGB masked", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()
