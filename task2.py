"""
2. Symulacja efektu "przepalenia" obrazu
a. Dodaj do każdego piksela wartość 150, ale używając NumPy.
b. Porównaj wynik z operacją cv2.add() .
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

M = np.ones(image.shape, dtype="uint8") * 150

added = image + M
opencv_added = cv2.add(image, M)

cv2.imshow("Added", added)
cv2.imshow("OpenCV Added", opencv_added)

cv2.waitKey(0)
