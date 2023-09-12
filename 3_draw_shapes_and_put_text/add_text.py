import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # shape(height,width,num_of_color_channels)
cv.imshow('Blank', blank)

"""5. Add text"""
# Write green Hello at the center of the image
cv.putText(blank, "Hello", org=(255, 255), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 255, 0),
           thickness=2)
cv.imshow("Hello", blank)

cv.waitKey(0)
