import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""1. Translation"""


def translate(img, x, y):
    """
    x,y are the number of pixels you are going to shift along the x-axis and y-axis
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[1])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 20)
cv.imshow('Translate_Silencer', translated)

translated2 = translate(img, -100, 20)
cv.imshow('Translate_Silencer2', translated2)

cv.waitKey(0)
