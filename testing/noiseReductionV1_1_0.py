#In this snippet we attempt to replicate the methods in:
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4752185/
#We first start to test how the gaussian filter affects the floc images
#

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../images/flocs/32903.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

#threshold: binary
retval,threshold =cv2.threshold(blur,140,255,cv2.THRESH_BINARY_INV)#below220: black higher:white
plt.subplot(223),plt.imshow(threshold),plt.title('Threshold')
plt.xticks([]), plt.yticks([])
plt.show()
#grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

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
