import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
# cv.imshow('Silencer', img)

# Convert the BGR image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""Sobel"""
sobelx = cv.Sobel(gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(gray, ddepth=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_and(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

cv.waitKey(0)
