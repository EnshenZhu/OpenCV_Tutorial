import cv2 as cv
import numpy as np

img = cv.imread('../Photos/dota_silencer.jpg')
# print(img.shape)
cv.imshow('Silencer', img)

"""5. Cropping"""
cropped = img[50:100, 100:200]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
