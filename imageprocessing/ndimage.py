from scipy import misc
import matplotlib.pyplot as plt
from scipy import ndimage

face = misc.face(gray= True)
face1 = ndimage.distance_transform_bf(face)

plt.figure()
plt.subplot(121)
plt.imshow(face)
plt.subplot(122)
plt.imshow(face1)
plt.show()


