#/usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('../images/flocs/32891.jpg')
blur = cv2.GaussianBlur(img,(5,5),0)
retval, img2 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

edges = cv2.Canny(img2,100,200)
cv2.imshow('closing',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
