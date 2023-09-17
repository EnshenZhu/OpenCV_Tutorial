import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""Split the image into three color channels"""
b, g, r = cv.split(img)  # split the image into blue,green and red

# The following displays show the pixel distribution intensities(corresponded color channels) in grayscale
# The light place in the image shows more concentration of the pixel values.
# The dark places shows little (or even no) pixels in that region
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)  # 3 color channels
print(b.shape)  # only 1 color channel (that is why it is shown as the grayscale)
print(g.shape)
print(r.shape)

"""Merge the three color channels"""
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)
