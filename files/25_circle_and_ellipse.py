import cv2
import numpy as np
image=cv2.imread('images/blobs.jpg',cv2.IMREAD_GRAYSCALE)
detector = cv2.SimpleBlobDetector_create()
keypoints=detector.detect(image)
blank=np.zeros( (1,1) )
blobs=cv2.drawKeypoints(image,keypoints,blank,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
no_of_blobs=len(blobs)
text='total no. of blobs detected : ' + str(len(keypoints))
cv2.putText(blobs,text,(50,450),cv2.FONT_HERSHEY_COMPLEX,1,(100,0,203),2)
cv2.imshow('blobs using default parameters ',blobs)
cv2.waitKey()

#set our filtering parameters
params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=1.0
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=False
params.filterByInertia=True
params.minInertiaRatio=0.01

detector=cv2.SimpleBlobDetector_create(params)
keypoints=detector.detect(image)
blank=np.zeros( (1,1) )
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
no_of_blobs=len(keypoints)
text="number of circular blobs : " + str(len(keypoints))
cv2.putText(blobs,text,(50,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,100,255),2)
cv2.imshow('filtering circular blobs only',blobs)
cv2.waitKey()


#set our filtering parameters
params=cv2.SimpleBlobDetector_Params()
params.filterByArea=True
params.minArea=10
params.filterByCircularity=True
params.minCircularity=0.01
params.filterByConvexity=False
params.filterByInertia=True
params.minInertiaRatio=0.02

detector=cv2.SimpleBlobDetector_create(params)
keypoints=detector.detect(image)
blank=np.zeros( (1,1) )
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
no_of_blobs=len(keypoints)
text="number of ellipse blobs : " + str(len(keypoints))
cv2.putText(blobs,text,(50,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,100,255),2)
cv2.imshow('filtering ellipticall blobs only',blobs)
cv2.waitKey()


cv2.destroyAllWindows()
