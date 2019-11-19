# Load two images
import cv2 as cv
img1 = cv.imread('cup.png')
img2 = cv.imread('dave.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
im1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
roi = im1[0:rows, 0:cols, ]
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
