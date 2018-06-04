import cv2
import numpy as np

body_classifier=cv2.CascadeClassifier('images/haarcascade_fullbody.xml')

cap=cv2.VideoCapture('images/pedestrians.mp4')

while cap.isOpened():
    ret,frame=cap.read()
    
    frame=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    bodies=body_classifier.detectMultiScale(gray,1.2,3)
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow('pedestrians',frame)
        
    if cv2.waitKey():
        break
    
cap.release()
cv2.destroyAllWindows()
