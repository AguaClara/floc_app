import skimage
import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('../images/flocs/Image 32381.jpg',0)
# on the left border
#img = cv2.imread('../images/flocs/Image 32406.jpg',0)


blur = cv2.GaussianBlur(img, (5,5), 10)

t2=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,7)

kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(t2,kernel,iterations = 2)



kernel = np.ones((4,4),np.uint8)

opened = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

kernel = np.ones((8,8),np.uint8)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

print(label(closed, connectivity = 1))

plt.subplot(221), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('closed')
plt.xticks([]), plt.yticks([])
plt.show()
