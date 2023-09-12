import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""4. Flipping"""
flip_vertically = cv.flip(img, flipCode=0)
# flipCode=0 --> flip the image vertically (over x-axis)
# vertically and horizontally
cv.imshow("Flip_Vertically", flip_vertically)

flip_horizontally = cv.flip(img, flipCode=1)
# flipCode=1 -->flip the image horizontally (over y-axis)
cv.imshow("Flip_Horizontally", flip_horizontally)

flip_both = cv.flip(img, flipCode=-1)
# flipCode=-1 --> flip both vertically and horizontally
cv.imshow("Flip_Both", flip_both)

cv.waitKey(0)
