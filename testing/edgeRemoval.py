#/usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,100,200)

edges = cv2.Canny(img_32891_closing,100,200)
cv2.imshow('closing',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
