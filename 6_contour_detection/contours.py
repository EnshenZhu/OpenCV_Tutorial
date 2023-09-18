import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# convert the image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# get the contour of the image via the Canny-edge detector
canny = cv.Canny(gray, threshold1=125, threshold2=175)
cv.imshow("Canny Edges", canny)

contours, hierarchies = cv.findContours(canny, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
# findContours function looks at the structure of the element or the edges we found in the image, and return the
# contours and the hierarchies.

print(f'{len(contours)} contour(s) found')

cv.waitKey(0)
