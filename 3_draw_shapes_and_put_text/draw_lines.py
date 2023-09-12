import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # shape(height,width,num_of_color_channels)
cv.imshow('Blank', blank)

"""4. Draw a line"""
# Draw a white line from the origin to the image center
cv.line(blank, pt1=(0, 0), pt2=(blank.shape[1] // 2, blank.shape[0] // 2), color=(255, 250, 255),
        thickness=3)
cv.imshow("White Line", blank)

# Draw another white line
cv.line(blank, pt1=(100, 250), pt2=(300, 400), color=(255, 250, 255),
        thickness=3)
cv.imshow("Add another White Line", blank)

cv.waitKey(0)
