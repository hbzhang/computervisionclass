import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
face = scipy.misc.face(gray=True)
lx, ly = face.shape
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
flip_ud_face = np.flipud(face)
rotate_face = ndimage.rotate(face, 45)
rotate_face_noreshape = ndimage.rotate(face, 45, reshape=False)
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.imshow(crop_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(flip_ud_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(rotate_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
left=0.01, right=0.99)
plt.show()
