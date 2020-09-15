"""
Extracting and Saving Frames From Video
"""

import cv2
import os

# Opens the Video file
cap = cv2.VideoCapture("video/p3.MOV")
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    path = 'train-data/p3' # To Choose File Location where you want to save JPG
    if ret == False:
        break
    cv2.imwrite(os.path.join(path, str(i)+'.jpg'), frame)
    i += 1

cap.release()
cv2.destroyAllWindows()