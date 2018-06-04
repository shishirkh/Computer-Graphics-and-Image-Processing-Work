import cv2
import numpy as np

image = cv2.imread('images/pyramid.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

orb=cv2.ORB_create()
keypoints=orb.detect(gray,None)
keypoints,descriptors=orb.compute(gray,keypoints)

print('no of keypoints detcted ',len(keypoints))
image=cv2.drawKeypoints(image,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('feature method - SIFT',image)
cv2.waitKey()
cv2.destroyAllWindows()

