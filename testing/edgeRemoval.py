import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
height, width = img.shape()

#Edges matrix to create mask
edges = cv2.Canny(closed, 130, 200)

mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)

#Top
for i in range width:
    if img(0,i) == 255:
        img_Out = cv2.floodFill(img, mask, (x,y), 0)

#Bottom

#Left

#Right
'''

img = cv2.imread('../images/flocs/Image 32381.jpg',0)
# on the left border
#img = cv2.imread('../images/flocs/Image 32406.jpg',0)

blur1 = cv2.bilateralFilter(img,5,10,10)
blur2 = cv2.GaussianBlur(img, (5,5), 10)

t1=cv2.adaptiveThreshold(blur1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,7)
t2=cv2.adaptiveThreshold(blur2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,7)


# kernel = np.ones((4,4),np.uint8)
# opened_1 = cv2.morphologyEx(t1, cv2.MORPH_OPEN, kernel)
# opened_2 = cv2.morphologyEx(t2, cv2.MORPH_OPEN, kernel)

kernel = np.ones((4,4),np.uint8)
dilation_1 = cv2.dilate(t1,kernel,iterations = 2)
dilation_2 = cv2.dilate(t2,kernel,iterations = 2)



kernel = np.ones((4,4),np.uint8)
opened_1 = cv2.morphologyEx(dilation_1, cv2.MORPH_OPEN, kernel)
opened_2 = cv2.morphologyEx(dilation_2, cv2.MORPH_OPEN, kernel)

kernel = np.ones((8,8),np.uint8)
closed_1 = cv2.morphologyEx(opened_1, cv2.MORPH_CLOSE, kernel)
closed_2 = cv2.morphologyEx(opened_2, cv2.MORPH_CLOSE, kernel)

height, width = closed_2.shape
print(height)
print(width)
output = closed_2.copy()
#Edges matrix to create mask
#edges = cv2.Canny(output, 130, 200)
#mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)

cv2.cvtColor(output,cv2.COLOR_GRAY2RGB)
mask = np.zeros((height+2,width+2), np.uint8)
#Top
diff = (6, 6, 6)
cv2.floodFill(output, mask, (955,279), [0,0,0])
print(output[955,279])

# i = 0
# while i < width:
#     if output[height-1,i].all() == 255:
#         output=cv2.floodFill(output, (height-1,i), 0 ,mask=null)
#     i = i+1

plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
# plt.subplot(232), plt.imshow(cv2.cvtColor(blur1, cv2.COLOR_GRAY2RGB)), plt.title('Bilateral')
# plt.xticks([]), plt.yticks([])
# plt.subplot(233), plt.imshow(cv2.cvtColor(blur2, cv2.COLOR_GRAY2RGB)), plt.title('Gaussian')
# plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(cv2.cvtColor(dilation_1, cv2.COLOR_GRAY2RGB)), plt.title('Bilateral dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(cv2.cvtColor(dilation_2, cv2.COLOR_GRAY2RGB)), plt.title('Gaussian dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(cv2.cvtColor(closed_1, cv2.COLOR_GRAY2RGB)), plt.title('Bilateral close')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(cv2.cvtColor(closed_2, cv2.COLOR_GRAY2RGB)), plt.title('Gaussian close')
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(cv2.cvtColor(output, cv2.COLOR_GRAY2RGB)), plt.title('output')
plt.xticks([]), plt.yticks([])
plt.show()


# rows,cols,channels=img.shape
# white=255

# Boundary floc removal
# uchar white(255);
#
# // do top and bottom row
# for(int y = 0; y < image.rows; y += image.rows-1)
# {
#     uchar* row = image.ptr<uchar>(y)
#     for(int x = 0; x < image.cols; ++x)
#     {
#         if(row[x] == white)
#         {
#             cv::floodFill(image, cv::Point(x,y), cv::Scalar(0), (cv::Rect*)0, cv::Scalar(), cv::Scalar(200));
#         }
#     }
# }
# // fix left and right sides
# for(int y = 0; y < image.rows; ++y)
# {
#     row = image.ptr<uchar>(y)
#     for(int x = 0; x < image.cols; x += image.cols - 1)
#     {
#         if(row[x] == white)
#         {
#             cv::floodFill(image, cv::Point(x,y), cv::Scalar(0), (cv::Rect*)0, cv::Scalar(), cv::Scalar(200));
#         }
#     }

#Old version
# ###### Loading image and thresholding
#
# #img = cv2.imread('../images/flocs/Image 32373.jpg',0)
# img = cv2.imread('../images/flocs/Image 32343.jpg',0)
#
#
# #switch it to greyscale
# #img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# blur = cv2.GaussianBlur(img, (11, 11), 0)
# #retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
#
#
# '''retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# t3=cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
#
# #th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# blur = cv2.GaussianBlur(img, (5, 5), 0)
# #retval, t1 = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)'''
#
#
# retval, t2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#

# # ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# #th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#
#
# thresh = t3
# ######
#
# print(thresh.shape)
#
# ##### Closing
# kernel = np.ones((4,4),np.uint8)
# opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#
# kernel = np.ones((13,13),np.uint8)
# closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
# #opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
#
#
# edges = cv2.Canny(closed, 130, 200)
# mask = np.pad(edges, pad_width=1, mode="constant", constant_values=0)
# fld_IMG = closed.copy()
#
#
# cv2.floodFill(fld_IMG, mask, (960, 100), (255,255,255))
# inverted_Flood = cv2.bitwise_not(fld_IMG)
# img_Out = (inverted_Flood | closed)
# '''cv2.imshow('closing', closed)
# cv2.imshow('t3', t3)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()'''
#
#
# plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(232), plt.imshow(cv2.cvtColor(t2, cv2.COLOR_GRAY2RGB)), plt.title('thresholding')
# plt.xticks([]), plt.yticks([])
# plt.subplot(233), plt.imshow(cv2.cvtColor(t3, cv2.COLOR_GRAY2RGB)), plt.title('gaussian thresholding')
# plt.xticks([]), plt.yticks([])
# plt.subplot(234), plt.imshow(cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)), plt.title('closed')
# plt.xticks([]), plt.yticks([])
# plt.subplot(235), plt.imshow(cv2.cvtColor(opened, cv2.COLOR_GRAY2RGB)), plt.title('opened')
# plt.xticks([]), plt.yticks([])
# plt.subplot(236), plt.imshow(cv2.cvtColor(blur, cv2.COLOR_GRAY2RGB)), plt.title('blur')
# plt.xticks([]), plt.yticks([])
#
# plt.show()
