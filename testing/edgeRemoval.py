# /usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/flocs/Image 32891.jpg')
blur = cv2.GaussianBlur(img, (5, 5), 0)
retval, img2 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

h, w = img2.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

#edges = cv2.Canny(img2,130,200)

fld_IMG = img2.copy()

border_point=(1::)
cv2.floodFill(fld_IMG, mask, border_point, (255,255,255))
#inverted_Flood = cv2.bitwise_not(fld_IMG)
img_Out = cv2.bitwise_not(fld_IMG | img2)
cv2.imshow('closing',img_Out)
cv2.waitKey(0)
cv2.destroyAllWindows()
