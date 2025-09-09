import cv2
import numpy as np
import matplotlib.pyplot as plt


print("Detecting keypoints and computing descriptors...")

im1 = cv2.imread("image/form.jpg")   # Template image
im2 = cv2.imread("image/scanned-form.jpg")   # Image to be aligned

plt.figure(figsize=[20, 10]);
plt.subplot(121); plt.axis('off'); plt.imshow(im1); plt.title("Original Form")
plt.subplot(122); plt.axis('off'); plt.imshow(im2); plt.title("Scanned Form")
plt.show()

im1_gray = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)
im2_gray = cv2.cvtColor(im2, cv2.COLOR_RGB2GRAY)

