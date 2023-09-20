import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# BGR to RGB
rgb = cv.cvtColor(img, code=cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# show the rgb_variable in the matplotlib
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
