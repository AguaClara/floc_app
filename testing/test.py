#/usr/local/bin/python

#show the picture
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''img = cv2.imread("t1.jpg", cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR=1
#IMREAD_UNCHANGED=-1
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



#show by plt
'''#x=[1,2,3]
#y=[2,3,4]
#plt.plot(x,y)
#plt.show()
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()'''

#draw/write on image

#img = cv2.imread("t1.jpg", cv2.IMREAD_GRAYSCALE)
'''draw:
# color : BGR green(0,255,0) white(255,255,255) black(0,0,0)
cv2.line(img,(0,0),(150,150),(255,255,255),15)# last line width
cv2.rectangle(img,(15,25),(300,400),(0,255,0),15)
cv2.circle(img,(100,100),100,(234,123,100),-1)#-1: fill in the circle
pts=np.array([[122,333],[12,45],[45,45],[64,111],[432,122]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)# true: connected begin end'''

#write:
'''font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(0,300),font,1,(255,100,300),2,cv2.LINE_AA)#2 thickness
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#image operations:
'''img = cv2.imread("t1.jpg",1)
img[55,55]=[255,255,255] #white pixel
px=img[55,55]#pixel
img[100:200,100:200]=[255,255,255]# ROI of image
# change pixel of image
face=img[300:400,200:400]
img[0:100,0:200]=face
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#image arithmetics and logic:
img1=cv2.imread('t1.jpg')
img2=cv2.imread('test.png')
#add=img1+img2
#weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
rows,cols,channels=img1.shape
roi=img1[0:rows,0:cols]
img1gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img1gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''# thresholding:
img=cv2.imread('t1.jpg')
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(grayscaled,190,255,cv2.THRESH_BINARY)#below220: black higher:white
#adaptive threshold
gaus=cv2.adaptiveThreshold(grayscaled,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#template matching:
img1=cv2.imread('t1.jpg')
img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
template=cv2.imread('template.png',0)
w, h = template.shape[::-1]
res=cv2.matchTemplate(img1_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.3
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img1,pt,(pt[0] + w, pt[1] + h), (0,255,255), 2)
cv2.imshow('detected',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#feature matching:
img1=cv2.imread('t3.jpg',1)
img2=cv2.imread('t4.jpg',1)
#detector
orb=cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None) #keypoint and descriptor
kp2, des2 = orb.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None, flags=2)
plt.imshow(img3)
plt.show()'''

#SURF (Speeded-Up Robust Features):
img=cv2.imread('/../images/t1.jpg')
retval,threshold=cv2.threshold(img,180,255,cv2.THRESH_BINARY)
surf = cv2.xfeatures2d.SURF_create(10000)
#keypoints and descriptors
kp, des = surf.detectAndCompute(threshold,None)
img2 = cv2.drawKeypoints(threshold,kp,None,(255,0,0),4)
plt.imshow(img2)
plt.show()


'''#denoise:
img = cv2.imread('t1.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,None,6,6,7,21)
retval,threshold=cv2.threshold(dst,190,255,cv2.THRESH_BINARY)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(threshold)
plt.show()'''
