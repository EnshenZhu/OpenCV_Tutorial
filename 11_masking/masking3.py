import cv2 as cv
import numpy as np

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Fengshen', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  # RECALL: img.shape is in the format of [row,column, color_channels]
# cv.imshow('Blank', blank)

"""Mask with a Rectangle"""
# create a circle
circle = cv.circle(blank.copy(), center=(img.shape[1] // 2 + 45, img.shape[0] // 2), radius=100, color=255,
                   thickness=-1)
cv.imshow('Circle', circle)

# create a rectangle
rectangle = cv.rectangle(blank.copy(), pt1=(30, 30), pt2=(370, 370), color=255, thickness=-1)
cv.imshow('Rectangle', rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)

# overlap two shapes together
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)
