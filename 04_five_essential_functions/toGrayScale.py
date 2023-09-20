import cv2 as cv

img = cv.imread('../Photos/roshan.jpeg')
cv.imshow('Cat', img)

"""1. Converting images to grayscale"""
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)
