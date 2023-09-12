import cv2 as cv

img = cv.imread('../Photos/roshan.jpeg')  # read the image
cv.imshow('Cat', img)  # display the image

cv.waitKey(0)  # keyboard binding function; let the program
# wait for specific amount of time before the keyboard is
# pressed. 0 means waiting for infinite amount of time for a
# key to be pressed.
