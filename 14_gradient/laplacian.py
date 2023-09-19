import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# Convert the BGR image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""Laplacian"""
lap = cv.Laplacian(gray, ddepth=cv.CV_64F)  # ddepth --> data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

cv.waitKey(0)
