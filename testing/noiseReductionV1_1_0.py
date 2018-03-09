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

img = cv2.imread('../images/flocs/Image 32830.jpg')

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
plt.show()

#adaptive threshold
#gaus=cv2.adaptiveThreshold(grayscaled,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#plt.imshow('original',img)
#plt.imshow('threshold',blur)
#cv2.imshow('gaus',gaus)
#plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()

'''#Morphological Transformations:
kernel = np.ones((5,5),np.uint8)

#closing:
closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
'''



'''# remove out of focus particles


'''
