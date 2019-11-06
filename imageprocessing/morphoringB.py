from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

face = misc.face(gray=True)
np.random.seed(0)
a = np.zeros((50, 50))
a[10:-10, 10:-10] = 1
a += 0.25 * np.random.standard_normal(a.shape)
mask = a>=0.5

opened_mask = ndimage.binary_opening(mask)
closed_mask = ndimage.binary_closing(opened_mask)

plt.figure()
plt.subplot(131)
plt.imshow(a)
plt.subplot(132)
plt.imshow(opened_mask)
plt.subplot(133)
plt.imshow(closed_mask)
plt.show()














