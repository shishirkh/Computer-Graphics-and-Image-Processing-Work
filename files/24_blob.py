import cv2
import numpy as np

image=cv2.imread('images/sunflower.jpg',cv2.IMREAD_GRAYSCALE)
                     
detector = cv2.SimpleBlobDetector_create()

keypoints=detector.detect(image)

blank=np.zeros( (1,1) )
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,255,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('blobs',blobs)
cv2.waitKey()
cv2.destroyAllWindows()
