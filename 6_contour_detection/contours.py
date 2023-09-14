import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# convert the image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# get the contour of the image via the Canny edge detector
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow("Canny Edges", canny)

contours, hierarchies = cv.findContours(canny, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)

cv.waitKey(0)
