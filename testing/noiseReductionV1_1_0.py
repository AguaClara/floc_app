# In this snippet we attempt to replicate the methods in:
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4752185/
# We want to try and perform noise reduction on the floc images to separate the
# foreground from the back ground, we also need to see how to properly deal
# with different flocs that are in and out of focus.
#
# Current Implementation:
# *We first start to test how the gaussian filter affects the floc images
# *We are applying inverse thresholding to the images and are currently testing
#     what values produce the best result

##############
import cv2
import numpy as np
from matplotlib import pyplot as plt
##############

=======
img = cv2.imread('../images/flocs/Image 32891.jpg')

# Application of the Gaussian Filter
blur = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

# Binary Inverse Thresholding
retval, threshold = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
plt.subplot(223), plt.imshow(threshold), plt.title('Threshold')
plt.xticks([]), plt.yticks([])

# remove out of focus particles: sobel filter
#laplacian = cv2.Laplacian(blur,cv2.CV_64F)
sobelx = cv2.Sobel(blur, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(sobelx, cv2.CV_64F,0,1,ksize=5)
plt.subplot(224), plt.imshow(laplacian, cmap='gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.show()

# Template Matching
w, h = img.shape[::-1]
res = cv2.matchTemplate(img, img, cv2.TM_CCOEFF_NORMED)
threshold = 0.3
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
