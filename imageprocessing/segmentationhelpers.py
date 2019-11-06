from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import skimage.transform


def generatebinaryimage():
    face =misc.face(gray=True)
    n = 10
    l = 256
    im = skimage.transform.resize(face, (l,l)) #np.zeros((l, l))
    np.random.seed(1)
    points = l*np.random.random((2, n**2))
    im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

    mask = (im > im.mean()).astype(np.float)
    mask += 0.2 * im
    img = mask + 0.2*np.random.randn(*mask.shape)

    hist, bin_edges = np.histogram(img, bins=60)
    bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

    binary_img = img > 0.5

    plt.figure()
    plt.subplot(131)
    plt.imshow(img)
    plt.subplot(132)
    plt.imshow(binary_img,cmap=plt.cm.gray)
    plt.subplot(133)
    plt.imshow(binary_img)
    plt.show()

