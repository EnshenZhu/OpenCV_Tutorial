import cv2 as cv

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Fengshen', img)

# Convert the BGR image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""Simple Thresholding"""
threshold, thresh = cv.threshold(gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)
# THRESH_BINARY --> equal or below 150 -> 0 | above 150 -> 255
# returned threshold -> same threshold value in the method (e.g., 150 in this case)
# returned thresh --> the threshold binary image
cv.imshow('Simple Thresholded', thresh)

# create an inverse thresholding
threshold, thresh_inv = cv.threshold(gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV)
# THRESH_BINARY_INV --> equal or below 150 -> 255 | above 150 -> 0
cv.imshow('Simple Thresholded Inversed', thresh_inv)

cv.waitKey(0)
