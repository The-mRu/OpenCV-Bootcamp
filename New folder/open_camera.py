# cv2.VideoCapture(0) → usually the default (built-in) webcam.

# cv2.VideoCapture(1) → often the first external webcam.

# cv2.VideoCapture(2) → if you have more cameras (like screen-capture drivers, virtual cams, etc.).

'''

import cv2
import sys

s = 1
if len(sys.argv) > 1:
    s = sys.argv[1]


source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)

'''


import cv2

cap = cv2.VideoCapture(1)

while cv2.waitKey(1) != 27:  # ESC to exit
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Camera", frame)

cap.release()
cv2.destroyAllWindows()
