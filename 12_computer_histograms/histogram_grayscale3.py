import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Fengshen', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank.copy(), center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=255, thickness=-1)
# cv.imshow('Circle', circle)

masked_img = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Mask', masked_img)

"""Grayscale histogram with the circle mask"""
gray_hist = cv.calcHist([gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])
# image and channels should be lists
# histSize --> number of bins that we want ot use for computing histogram (in the list format)
# ranges --> ranges of all possible pixel values

plt.figure()
plt.title('Grayscale Histogram with the Circle Mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
