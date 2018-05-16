from skimage.measure import label, regionprops
from skimage.segmentation import clear_border
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

img = cv2.imread('../images/flocs/Image 32419.jpg',0)
blur = cv2.GaussianBlur(img, (5,5), 10)

t2=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,7)
t3=cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('img')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('closed')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(cv2.cvtColor(cleared, cv2.COLOR_GRAY2RGB)), plt.title('cleared')
plt.xticks([]), plt.yticks([])
plt.show()
