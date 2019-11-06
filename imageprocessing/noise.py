from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
face = misc.face(gray=True).astype(float)
face = face[230:290, 220:320]
face = face + 0.5*face.std()+ np.random.random(face.shape)

smooth = ndimage.gaussian_filter(face, 2)
filtered = ndimage.median_filter(face,2)

plt.figure()
plt.subplot(131)
plt.imshow(face,cmap=plt.cm.gray)
plt.subplot(132)
plt.imshow(smooth, cmap=plt.cm.gray)
plt.subplot(133)
plt.imshow(filtered,cmap=plt.cm.gray)
plt.show()




