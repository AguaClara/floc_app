from skimage.measure import label, regionprops
from skimage.segmentation import clear_border
import cv2
import numpy as np
from matplotlib import pyplot as plt




img = cv2.imread('../images/flocs/Image 32795.jpg',0)
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

cleared = closed.copy()
cleared=clear_border(cleared)

labels=label(cleared, connectivity = 1)

print('regions number:',labels.max())
# The properities of images
for region in regionprops(labels):
    print(region.area) #循环得到每一个连通区域属性集




plt.subplot(121), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('closed')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cleared, cv2.COLOR_GRAY2RGB)), plt.title('cleared')
plt.xticks([]), plt.yticks([])

plt.show()
