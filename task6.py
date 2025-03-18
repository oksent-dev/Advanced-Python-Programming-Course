"""
6. Automatyczne skalowanie na podstawie wysokości
a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
b. Wyświetl wynik.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized = imutils.resize(image, height=400)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
