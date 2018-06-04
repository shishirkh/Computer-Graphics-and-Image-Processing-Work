import cv2
import numpy as np

image=cv2.imread('images/pyramid.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

surf=cv2.xfeatures2d.SURF_create()
#only features whose hessian is larger than hessianThreshold are retained by the detector
surf.setHessianThreshold(5700)
keypoints,descriptors=surf.detectAndCompute(gray,None)

print('no of keypoints detected : '+str(len(keypoints)))
image=cv2.drawKeypoints(image,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('feature method - SIFT',image)
cv2.waitKey()
cv2.destroyAllWindows()

