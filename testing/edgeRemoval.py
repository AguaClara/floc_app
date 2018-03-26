# /usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

###### Loading image and thresholding
img = cv2.imread('../images/flocs/Image 32373.jpg',0)

#switch it to greyscale
#img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img, (5, 5), 0)
#retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)


retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t3=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

thresh = t3
######

print(thresh.shape)

##### Closing
kernel = np.ones((5,5),np.uint8)
closed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#closed = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

>>>>>>> 0f966c653c5c41430725d9de9c2d9ff43de6d93c
edges = cv2.Canny(closed, 130, 200)
mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)
fld_IMG = closed.copy()


cv2.floodFill(fld_IMG, mask, (960, 100), (255,255,255))
inverted_Flood = cv2.bitwise_not(fld_IMG)
img_Out = (inverted_Flood | closed)
'''cv2.imshow('closing', closed)
cv2.imshow('t3', t3)
>>>>>>> 0f966c653c5c41430725d9de9c2d9ff43de6d93c
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
plt.subplot(235), plt.imshow(cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)), plt.title('edges')
plt.xticks([]), plt.yticks([])
plt.show()
