import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # shape(height,width,num_of_color_channels)
cv.imshow('Blank', blank)

"""1. Paint the image into a certain color"""
blank[:] = 0, 255, 0  # green
cv.imshow('Green', blank)

blank[:] = 0, 0, 255  # red
cv.imshow('Red', blank)

blank[:] = 255, 0, 0  # blue
cv.imshow('Blue', blank)

# paint the image with a certain portion
blank[200:300, 300:400] = 0, 0, 255  # part of red
cv.imshow('Part of Red', blank)

# img = cv.imread('../Photos/roshan.jpeg')
# cv.imshow('Cat', img)

cv.waitKey(0)