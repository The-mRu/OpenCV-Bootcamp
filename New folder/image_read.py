import cv2

# Load image
img = cv2.imread("image/messi.jpg")

# Show image
cv2.imshow("Test Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
