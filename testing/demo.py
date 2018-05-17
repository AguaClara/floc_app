from skimage.measure import label, regionprops
from skimage.segmentation import clear_border
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

#img = cv2.imread('../images/flocs/Image 32419.jpg',0)
#img = cv2.imread('../images/flocs/Image 32406.jpg',0)
#img = cv2.imread('../images/flocs/Image 32379.jpg',0)
img = cv2.imread('../images/flocs/Image 32427.jpg',0)
blur = cv2.GaussianBlur(img, (5,5), 10)

t2=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,7)
retvel,t3=cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

# plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('Original Image')
# plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(cv2.cvtColor(t2, cv2.COLOR_GRAY2RGB)), plt.title('Local thresholding')
# plt.xticks([]), plt.yticks([])
# plt.subplot(133), plt.imshow(cv2.cvtColor(t3, cv2.COLOR_GRAY2RGB)), plt.title('Global thresholding')
# plt.xticks([]), plt.yticks([])
# plt.show()

kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(t2,kernel,iterations = 2)

kernel = np.ones((4,4),np.uint8)
opened = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

kernel = np.ones((8,8),np.uint8)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

cleared = closed.copy()
cleared=clear_border(cleared)

kernel = np.ones((10,10),np.uint8)
opened_2 = cv2.morphologyEx(cleared, cv2.MORPH_OPEN, kernel)

labels=label(opened_2, connectivity = 2)

area=[]
print('regions number:',labels.max())
# The properities of images
for region in regionprops(labels):
    area.append(region.area)

print(area)
# cv2.imwrite('../images/final/32904 thresholding.png',img)
# plt.subplot(221), plt.imshow(cv2.cvtColor(t2, cv2.COLOR_GRAY2RGB)), plt.title('Local Thresholding')
# plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_GRAY2RGB)), plt.title('Dilation')
# plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(cv2.cvtColor(opened, cv2.COLOR_GRAY2RGB)), plt.title('Opening')
# plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('Closing')
# plt.xticks([]), plt.yticks([])
# plt.show()
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv2.cvtColor(opened_2, cv2.COLOR_GRAY2RGB)), plt.title('Border floc removal')
plt.xticks([]), plt.yticks([])

plt.show()
