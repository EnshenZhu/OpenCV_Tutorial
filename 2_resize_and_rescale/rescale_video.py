import cv2 as cv


# primary way of rescale
def rescaleFrame(frame, scale=0.75):
    # It works for Images, Videos and Live videos
    """
    frame.shape[1] -> original width of the image
    frame.shape[0] -> original height of the image
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# another way of rescale (ONLY for Live Videos, not for images)
def changeRes(width, height):
    capture.set(3, width)  # 3 refers to the width
    capture.set(4, height)  # 4 refers to the height


capture = cv.VideoCapture('../Videos/ship.MOV')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)  # resize to the original video into 0.75
    frame_resized_25 = rescaleFrame(frame, scale=0.25)  # resize to the original video into 0.25

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    cv.imshow("Video_resized_25", frame_resized_25)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
