import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

"""We are going to use this blank variable as a basis to draw a rectangle and a circle"""

rectangle = cv.rectangle(blank.copy(), pt1=(30, 30), pt2=(370, 370), color=255, thickness=-1)
circle = cv.circle(blank.copy(), center=(200, 200), radius=200, color=255, thickness=-1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)
# cv.imshow('Blank', blank)

# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> non-intersecting regions
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not_circle)

cv.waitKey(0)
