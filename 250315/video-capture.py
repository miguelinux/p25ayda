#!/usr/bin/env python

"""
Taken from : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
"""

import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow("frame", gray)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
