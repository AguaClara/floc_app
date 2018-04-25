'''
Steps:
1. Identify all edges in images
2. If the gradient over an "edge pixel" meets a certain thresholding
    3. Floodfill everything inside this flocs' edge white
4. Make everything else black
5. Hopefully this will work?????? PLS PLS PLS WORK PLEASE WORK FOR ME PLEASE
PRETTY PLEASE WORK!!!!!
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../images/flocs/Image 32381.jpg",0)
