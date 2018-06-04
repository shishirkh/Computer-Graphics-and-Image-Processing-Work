dilation : adds pixels to the boundary of objects
erosion : remove pixels to the boundary of objects
opening : erosion followed by dilation
closing : dilation followed by erosion

approximation methods in contourings
cv2.CHAIN_APPROX_NONE : stores all the points that make up a line segment
cv2.CHAIN_APPROX_SIMPLE : stores only the start and end of a line segment(efficient)

sorting contours
-> sorting by area
-> sorting by spatial positions

cropping each contour in an image

if we use a whte background, then the whole white background is also considered as a separate contour
so use : n=len(contours) - 1

cv2.moments(contour)
cv2.drawContour : to dram lines

to get moment : 
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])

LINE DETECTION:
hough lines
probabilistic houghh lines
 
BLOB DETECTION:
create detector,input image into the detector,obtain the key points,draw those key points

is_v2 = cv2.__version__.startswith("2.")
if is_v2:
    detector = cv2.SimpleBlobDetector()
else:
    detector = cv2.SimpleBlobDetector_create()

cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the soze of that blob

BLOB FILTERING:

cv2.SimpleBlobDetector_Params()

AREA:
params.filterByArea=True/False
params.minArea=pixels
params.maxArea=pixels
CIRCULARITY:
params.filterByCircularity=True/False
params.minCircularity=1 (perfect circle) 0 (not the perfect circle)
CONVEXITY:
---> area_of_blob/area_of_convex_hull
params.filterByConvexity=True/False
params.minConvexity=0 to 1
INERTIA:
measure of ellipticalness(LOW being more elliptical,HIGH being less elliptical)
params.filterByInertia=True/False
params.minInertiaRatio=0.01 (0==>straight line and 1==>circle)


OBJECT DETECTION USING A CROPPED IMAGE DOES NOT ALWAYS GIVE GOOD RESULTS AS :
1. rotation renders this method ineffective
2. scaling affects the results tremendously
3. changes in quality--brightness,contrast affect it
4. a different angle of view gives different results - not reliable

ALTERNATIVE METHODS :
image features : 
interesting areas that are somewhat unique to that image
features unique to soomething like taj mahal can be stored and can 
be used in the future to tell whether a image is of
taj mahal or not using these unique features

also can be used for STITCHING IMAGES TOGETHER...panaroma stitching

HOW TO DECIDE WHETHER SOMETHING IS INTERESTING OR NOT:
interesting areas carry alot of distinct and unique information at that point
-high changes of intensity
-corners
-sometimes NOISE may also be labeled as Interesting

CHARACTERISTICS OF GOOD OR INTERESTING FEATURES
1. REPEATABLE : can be found in multiple pictures of the same scene
2. DISINCTIVE : unique and differs from other features found in the scene
3. COMPACTNESS : less pic=xels than the original pixels
4. LOCALITY : free from clutter and small in dimensions

CORNERS AS FEATURES
corners are identified when shifting a window in any direction over that point gives 
a large change in intensity
edges give such a change in only one direction
corner gives change in all directions

corner matching in images is tolerant of rotations translations slight changes in brightness intensity

however it is intolerant of large changes in intensity or brightness
scaling

enlarging results in more corners being detected

solutions to the above problems
some other detectors....
SIFT : SCALE INVARIANT FEATURE TRANSFORM
gives us the needed tolerance to scalingw
SURF : SPEEDED UP ROBUST FEATURES
was developed to imporve the speed of a SIFT
FAST : FEATURES FROM ACCELEREATED SEGMENT TEST
key point detections only
used in real time applications
BRIEF : BINARY ROBUST INDEPENDENT ELEMENTARY FEATURES
computes desciptors quickly
ORB : ORIENTED FAST AND ROTATED BRIEF
combines both FAST and BRIEF
default number of points ORB detects = 500

descriptors are things which store information vectors which store info about 
the points!!
to do any matching between images we do matching between their descriptor


FLANN BASED MATCHER


HOGS : histogram of oriented gradients


HAAR CASCADE FEATURES

detectMultiScale : - > Scale Factor-specifies how much we reduce the size of the image 
				    we scale, e.g. in face detection we typically use 1.3 whch means
				    we have reduced the image by 30% each time it's scaled.
- > min neighbors - specifies the no of neighbors each potential window should have in order to consider it a positive detection
