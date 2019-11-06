from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

im = np.zeros((255,255))
np.random.seed(1)
x, y = 255*np.random.random((2, 100)).astype(np.int)
print(x.shape)
#im[x, y] = 1
im[(x).astype(np.int), (y).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=256/(40.0))
mask = (im > im.mean()).astype(np.float)
mask += 0.1 * im
img = mask + 0.2*np.random.randn(255,255)
hist, bin_edges = np.histogram(img, bins=60)

bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])
binary_img = img > 0.5
open_img = ndimage.binary_opening(binary_img)

plt.figure()
plt.subplot(131)
plt.imshow(img)
plt.subplot(132)
plt.imshow(binary_img)
plt.subplot(133)
plt.imshow(open_img)
plt.show()

