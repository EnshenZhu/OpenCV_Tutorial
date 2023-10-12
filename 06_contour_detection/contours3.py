import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# convert the image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

"""Try to distinguish the difference between Canny"""
# get the contour of the image via the Canny edge detector
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow("Canny Edges", canny)

"""Create an extra blank image"""

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow("Blank", blank)

ret, thresh = cv.threshold(gray, thresh=125, maxval=255, type=cv.THRESH_BINARY)
# if the image value is equal ot below 125, set it into black --> 0
# if the image value is over 125, set it into white --> 255
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(thresh, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)
# findContours function looks at the structure of the element or the edges we found in the image, and return the
# contours and the hierarchies.

print(f'{len(contours)} contour(s) found')

"""Draw the contour on the blank image"""
cv.drawContours(blank, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)
# contourIdx --> how many contours we want in the image, (specify -1 to draw all contours)

cv.imshow("Contour Drawn", blank)

cv.waitKey(0)
