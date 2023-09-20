import cv2 as cv
import numpy as np

"""This script is going to display the original image for a specific color channel"""

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

"""Split the image into three color channels"""
b, g, r = cv.split(img)  # split the image into blue,green and red

blue = cv.merge([b, blank, blank])  # set the green and red channel to black, and only display the blue channel
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue_sync', blue)
cv.imshow('Green_sync', green)
cv.imshow('Red_sync', red)

"""Merge the three color channels"""
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)
