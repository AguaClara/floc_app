'''
Steps:
1. Identify all edges in images
2. If the gradient over an "edge pixel" meets a certain thresholding
    3. Floodfill everything inside this flocs' edge white
4. Make everything else black
5. Hopefully this will work?????? PLS PLS PLS WORK PLEASE WORK FOR ME PLEASE
PRETTY PLEASE WORK!!!!!
'''
import numpy as np
import skimage
from skimage import io
from skimage.feature import canny
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.filters import sobel
from skimage.segmentation import watershed

img = io.imread('../images/flocs/Image 32795.jpg')
edges = canny(img, sigma=4.)

markers = np.zeros_like(img)
markers[img < 30] = 1
markers[img > 200] = 2
elevation_map = sobel(img)
segmentation = watershed(img, markers)

fig, (ax1,ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
sharex=True, sharey=True)
ax1.imshow(img, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('Original Image', fontsize=10)

ax2.imshow(edges, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Edges Image', fontsize=10)

ax3.imshow(segmentation, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Edges Image', fontsize=10)

plt.show()
