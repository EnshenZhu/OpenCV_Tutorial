import cv2 as cv
import numpy as np

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Silencer', img)

# Averaging
average = cv.blur(img, ksize=(3, 3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=0)  # sigmaX is the std in the x-axis
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, ksize=3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, d=10, sigmaColor=35, sigmaSpace=25)
"""d --> It is NOT the kernel size, but the diameter. sigmaColor --> Color sigma; a large sigmaColor value means that 
there are more colors in the neighborhood that will be considered when the blur is computed. sigmaSpace --> Space 
sigma; a large sigmaSpace value means pixels further out from the central pixel will influence the central 
calculation."""
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
