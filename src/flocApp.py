'''
This file holds all the relavant scripts for the FLoc App under Agua Clara
    Functions:
    Examples:
    Dependencies:
                                                                Cheers,
                                                                -Floc App Team
'''

# Start of Imports
import glob
import cv2
import numpy as np
from matplotlib import pyplot as plt
# End of Imports

'''
Purpose:
    - The applyTo function will open the folder at the provided path and then
    apply a given function to all the photos in the folder
Parameters:
    - Path to folder ex: "usr/aguaclara/documents/images"
    - Note the images should be .jpg
    - Function f
Returns:
    - Whatever f would have outputted
Raises:
    -
'''
def applyTo(path, fcn):
    for file in glob.glob(os.path.join(path, "*.jpg")):
        fcn(file)

'''
Purpose:
    - Given an image of a floc, will apply a set of image proccessing Functions
    to identify in focus flocs from the background.
Parameters:
    - A .jpg image read in as a grayscale image i.e cv2.imread('path',0)
Returns:
    - A processed .jpg image
Raises:
    -
'''
def flocID(img):
    blur = cv2.GaussianBlur(img, (5,5), 10)
    t = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                    cv2.THRESH_BINARY_INV,9,7)
    kernel = np.ones((4,4),np.uint8)
    dilation = cv2.dilate(t,kernel,iterations = 2)
    opened = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    return closed

'''
Purpose:
    - Simple function that can compare two given images using matplotlib
Parameters
    - Two .jpg images
Returns:
    - Opens a pyplot showing the two images
Raises:
    - 
'''
def compareImg(img1, img2):
    plt.subplot(121),
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)), plt.title('Image 1')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232),
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)), plt.title('Image 2')
    plt.xticks([]), plt.yticks([])
    plt.show()
