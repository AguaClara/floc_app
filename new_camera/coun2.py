import sys
import cv2
import numpy as np
from PIL import Image


def read_image(image_path):
    """Read an image into a numpy array.
    Args:
      image_path: Path to the image file.

    Returns:
      Numpy array containing the image
    """
    img = cv2.imread(image_path, 0)
    return img


def whitePixels(grid):
    """Count number of all white pixels(RGB > 225)"""
    img = np.where(grid > 225, grid, 0)
    return img


img = read_image("image2.jpg")
# print(img)
result = whitePixels(img)
print(result)
cv2.imwrite('imagetest2.jpg', result)
