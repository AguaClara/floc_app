import cv2
import numpy
import wx


cap = cv2.VideoCapture("sample.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)

    if ret==True:
        cv2.imshow('fgmask',fgmask)
        cv2.imshow("original", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    

cap.release()
cv2.destroyAllWindows()