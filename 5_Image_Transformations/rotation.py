import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""2. Rotation"""


# OpenCV allows you to rotate the image in respect to any point

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # the rotation point is default to be the center of the image
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(center=rotPoint, angle=angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)  # positive rotate angle --> counterclockwise
cv.imshow("Rotated", rotated)

reverse_rotated = rotate(img, -45)
cv.imshow("Reverse_Rotate", reverse_rotated)  # negative rotate angle --> clockwise

cv.waitKey(0)
