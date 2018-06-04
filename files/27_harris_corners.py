import cv2
import numpy as np
image=cv2.imread('images/chess.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# H A R R I S CORNER
harris_corners=cv2.cornerHarris(gray,3,3,0.05)
kernel=np.ones( (7,7),np.uint8 )
harris_corners=cv2.dilate(harris_corners,kernel,iterations=2)
image[harris_corners > 0.025 * harris_corners.max()]=[255,127,127]
cv2.imshow('harris corners',image)
cv2.waitKey()

# G O O D FEATURES
gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,100,0.01,150)
for corners in corners:
    x,y=corners[0]
    x=int(x)
    y=int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,255,0,),2)

cv2.imshow('harris corners',image)
cv2.waitKey()
cv2.destroyAllWindows()

