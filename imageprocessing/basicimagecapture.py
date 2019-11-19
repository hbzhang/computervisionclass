import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret is not None:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        cv2.imwrite("result.png", frame)
        cv2.imshow("me", frame)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            sys.exit()
            #break

cap.release()
cap.destroyAllWindows()
