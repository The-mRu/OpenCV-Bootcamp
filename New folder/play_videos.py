import os
import cv2
import sys

# Load the video file
video_path = 'videos/race_car.mp4'
if not os.path.exists(video_path):
    print(f"Error: The video file '{video_path}' does not exist.")
    sys.exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()

while cv2.waitKey(1) != 27:  # ESC to exit
    ret, frame = cap.read() # Read a frame from the video file
    if not ret: 
        print("Finished playing video.")
        break
    cv2.imshow("Video Playback", frame) 
cap.release()
cv2.destroyAllWindows()
    
    