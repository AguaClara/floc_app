

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

# Binary Inverse Thresholding
