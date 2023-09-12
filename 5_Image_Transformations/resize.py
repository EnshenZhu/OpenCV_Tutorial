import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""3. Resizing"""
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

cv.waitKey(0)
