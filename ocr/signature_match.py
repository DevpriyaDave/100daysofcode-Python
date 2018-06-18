import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/Users/devpriyadave/git/python/ocr/static/dl1.jpeg',0)
img2 = cv2.imread('/Users/devpriyadave/git/python/ocr/static/dl2.jpeg',0)


orb = cv2.ORB_create()


kp1 = orb.detect(img1,None)
kp2 = orb.detect(img2,None)
kp1, des1 = orb.compute(img1,kp1)
kp2, des2 = orb.compute(img2, kp2)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


matches = bf.match(des1,des2)


matches = sorted(matches, key=lambda x: x.distance)


img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

plt.imshow(img3),
plt.show()
