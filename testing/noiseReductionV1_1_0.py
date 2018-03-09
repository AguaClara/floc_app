#In this snippet we attempt to replicate the methods in:
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4752185/
#We first start to test how the gaussian filter affects the floc images
#

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../images/t1.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()










'''#threshold: binary
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(grayscaled,190,255,cv2.THRESH_BINARY_INV)#below220: black higher:white
#adaptive threshold
gaus=cv2.adaptiveThreshold(grayscaled,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
