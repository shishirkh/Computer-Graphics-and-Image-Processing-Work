import cv2
import numpy as np
image=cv2.imread('images/waldo.jpg')
cv2.imshow('where is waldo?',image)
cv2.waitKey()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
template=cv2.imread('images/template_waldo.jpeg',0)
cv2.imshow('template',template)
cv2.waitKey()

result=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)

top_left=max_loc
bottom_right=( top_left[0]+90,top_left[1]+90)
cv2.rectangle(image,top_left,bottom_right,(0,0,255),2)

cv2.imshow('where is waldo answered!!!',image)
cv2.waitKey()
cv2.destroyAllWindows()


cv2.destroyAllWindows()
 