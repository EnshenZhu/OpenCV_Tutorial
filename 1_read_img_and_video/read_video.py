import cv2 as cv

capture = cv.VideoCapture('../Videos/ship.MOV')
# The capture variable is an instance of the VideoCapture clause

while True:
    isTrue, frame = capture.read()  # grab the video frame by frame
    cv.imshow('Video', frame)  # display each frame of the video
    if cv.waitKey(20) & 0xFF == ord('d'):  # if the key 'd' is pressed, then break out the loop
        break

capture.release()
cv.destroyAllWindows()
