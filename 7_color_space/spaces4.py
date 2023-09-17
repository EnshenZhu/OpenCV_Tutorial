import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

plt.imshow(img)
plt.show()

cv.waitKey(0)
