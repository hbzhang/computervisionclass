from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

face = misc.face(gray=True)
#face1 = ndimage.binary_erosion(face, structure=np.ones((225,225))).astype(face.dtype)
#face2 = ndimage.binary_dilation(face, structure=np.ones((5,5))).astype(face.dtype)
#face3 = ndimage.binary_opening(face, structure=np.ones((3,3))).astype(face.dtype)


smallimage = np.zeros((32,32))
smallimage[10:-10, 10:-10] = 1
np.random.seed(2)
x, y = (32*np.random.random((2, 20))).astype(np.int)
smallimage[x, y] =1
open_square = ndimage.binary_opening(smallimage)
open_square1 = ndimage.binary_erosion(open_square)
recontruction = ndimage.binary_propagation(open_square1)


plt.figure()
plt.subplot(141)
plt.imshow(smallimage, cmap=plt.cm.gray)
plt.subplot(142)
plt.imshow(open_square,cmap=plt.cm.gray)
plt.subplot(143)
plt.imshow(open_square1, cmap=plt.cm.gray)
plt.subplot(144)
plt.imshow(recontruction, cmap=plt.cm.gray)
plt.show()
