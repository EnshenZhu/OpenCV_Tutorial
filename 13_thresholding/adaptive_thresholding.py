import cv2 as cv

img = cv.imread('../Photos/fengshen.jpg')
# cv.imshow('Fengshen', img)

# Convert the BGR image to grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""Adaptive Thresholding"""
adaptive_thresh = cv.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                                       thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=9)
# blockSize --> the kernel size that the OpenCV need to use compute the mean and find the threshold value.
# C --> an integer that is subtracted from the mean, allowing us to fine tune of the threshold.
cv.imshow('Adaptive Thresholding', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=9)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)
