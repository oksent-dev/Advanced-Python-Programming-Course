"""
1. Porównanie metod dodawania
a. Wczytaj obraz i zwiększ jego jasność o 50 przy użyciu zarówno NumPy,
jak i OpenCV.
b. Sprawdź, jak różnią się wyniki.
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

M = np.ones(image.shape, dtype="uint8") * 50
added = image + M
opencv_added = cv2.add(image, M)

cv2.imshow("Added", added)
cv2.imshow("OpenCV Added", opencv_added)

cv2.waitKey(0)
cv2.destroyAllWindows()
