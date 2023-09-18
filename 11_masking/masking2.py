import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  # RECALL: img.shape is in the format of [row,column, color_channels]
# cv.imshow('Blank', blank)

"""Mask with a Rectangle"""
mask = cv.rectangle(blank.copy(), pt1=(img.shape[1] // 2, img.shape[0] // 2),
                    pt2=(img.shape[1] // 2 + 100, img.shape[0] // 2 + 100), color=255, thickness=-1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)
