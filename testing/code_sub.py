

import cv2
import numpy as np
from matplotlib import pyplot as plt

# The image processing of image 32891:

# Import of image
img_32891_orig = cv2.imread('../images/flocs/Image 32891.jpg')

plt.subplot(221), plt.imshow(img_32891_orig), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Application of the Gaussian Filter
img_32891_blur = cv2.GaussianBlur(img_32891_orig, (5, 5), 0)

plt.subplot(222), plt.imshow(img_32891_blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

# Binary Inverse Thresholding after filter
retval, img_32891_threshold = cv2.threshold(img_32891_blur, 130, 255, cv2.THRESH_BINARY_INV)
plt.subplot(223), plt.imshow(img_32891_threshold), plt.title('Threshold')
plt.xticks([]), plt.yticks([])


# Morphological Transformations
# closing: closing small holes inside the object
kernel = np.ones((5,5),np.uint8)
img_32891_closing = cv2.morphologyEx(img_32891_threshold, cv2.MORPH_CLOSE, kernel)

plt.subplot(224), plt.imshow(img_32891_closing), plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.show()
