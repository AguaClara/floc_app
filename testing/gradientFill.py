'''
Steps:
1. Identify all edges in images
2. If the gradient over an "edge pixel" meets a certain thresholding
    3. Floodfill everything inside this flocs' edge white
4. Make everything else black
5. Hopefully this will work?????? PLS PLS PLS WORK PLEASE WORK FOR ME PLEASE
PRETTY PLEASE WORK!!!!!
'''
import cv2
import numpy as np
import skimage
from skimage import io
from skimage.feature import canny
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.filters import sobel
from skimage.segmentation import watershed

img = io.imread('../images/flocs/Image 32373.jpg')
blur = cv2.GaussianBlur(img, (5,5), 10)
t = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY_INV,9,7)
kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(t,kernel,iterations = 2)
opened = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
kernel = np.ones((8,8),np.uint8)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

fig, (ax1,ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
sharex=True, sharey=True)
ax1.imshow(img, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Original Image', fontsize=10)

ax2.imshow(opened, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Edges Image', fontsize=10)

ax3.imshow(closed, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Edges Image', fontsize=10)

plt.show()
