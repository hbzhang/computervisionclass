from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

face = misc.face(gray=True)
im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
facerotated = ndimage.rotate(face, 15, mode="constant")
facefiltered = ndimage.gaussian_filter(facerotated, 5)
sobelx = ndimage.sobel(im, axis=0, mode ="constant")
sobely = ndimage.sobel(im, axis=1, mode ="constant")
sobel = np.hypot(sobelx,sobely)

plt.figure()
plt.subplot(331)
plt.imshow(face, cmap = plt.cm.gray)
plt.subplot(332)
plt.imshow(facerotated, cmap =plt.cm.gray)
plt.subplot(333)
plt.imshow(facefiltered, cmap = plt.cm.gray)
plt.subplot(335)
plt.imshow(sobelx, cmap=plt.cm.gray)
plt.subplot(336)
plt.imshow(sobely, cmap = plt.cm.gray)
plt.subplot(338)
plt.imshow(sobel, cmap = plt.cm.gray)
plt.show()


