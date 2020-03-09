import sys
import cv2
import numpy as np
from PIL import Image

# Mat src, src_gray
# Mat dst, detected_edges

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

def canny_edge(grid):
    """Canny edge detector"""
    edge= cv2.Canny(grid, 100, 200)
    return edge

def detect_areas(grid):
    """Canny edge detector"""
    acc = []
    for area in cv2.findContours(canny_edge(grid), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE):
        acc.append(area)
    return acct

img = read_image("image2.jpg")
# print(img)
result = whitePixels(img)
print(result)
cv2.imwrite('imagetest2.jpg', result)
cv2.imwrite('canny_edge.jpg', canny_edge(img))
print(detect_areas(img))
