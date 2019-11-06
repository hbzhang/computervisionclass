from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt
face = misc.face(gray=True).astype(float)
blurred_f = ndimage.gaussian_filter(face, 3)
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
alpha = 30
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.imshow(blurred_f, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(filter_blurred_f, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(sharpened, cmap=plt.cm.gray)
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
left=0.01, right=0.99)
plt.show()


