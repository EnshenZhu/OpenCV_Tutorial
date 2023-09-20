import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# convert the image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

ret, thresh = cv.threshold(gray, thresh=125, maxval=255, type=cv.THRESH_BINARY)
# if the image value is equal or below 125, set it into black --> 0
# if the image value is over 125, set it into white --> 255
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(thresh, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
# findContours function looks at the structure of the element or the edges we found in the image, and return the
# contours and the hierarchies.

print(f'{len(contours)} contour(s) found')

cv.waitKey(0)
