# /usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

###### Loading image and thresholding

img = cv2.imread('../images/flocs/Image 32373.jpg',0)
#img = cv2.imread('../images/flocs/Image 32343.jpg',0)


#switch it to greyscale
#img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img, (21, 21), 0)
#retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)


'''retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t3=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
blur = cv2.GaussianBlur(img, (5, 5), 0)
#retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)'''


retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t3=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,2)
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


thresh = t3
######

print(thresh.shape)

##### Closing
kernel = np.ones((4,4),np.uint8)
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

kernel = np.ones((13,13),np.uint8)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
#opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)


edges = cv2.Canny(closed, 130, 200)
mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)
fld_IMG = closed.copy()


cv2.floodFill(fld_IMG, mask, (960, 100), (255,255,255))
inverted_Flood = cv2.bitwise_not(fld_IMG)
img_Out = (inverted_Flood | closed)
'''cv2.imshow('closing', closed)
cv2.imshow('t3', t3)

cv2.waitKey(0)
cv2.destroyAllWindows()'''


plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(cv2.cvtColor(t2, cv2.COLOR_GRAY2RGB)), plt.title('thresholding')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(cv2.cvtColor(t3, cv2.COLOR_GRAY2RGB)), plt.title('gaussian thresholding')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('closed')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(cv2.cvtColor(opened, cv2.COLOR_GRAY2RGB)), plt.title('opened')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB)), plt.title('blur')
plt.xticks([]), plt.yticks([])

plt.show()
