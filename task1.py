"""
1. Zmniejszenie obrazu o połowę
a. Wczytaj obraz i zmniejsz jego szerokość oraz wysokość o 50%.
b. Wyświetl wynik.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized = imutils.resize(
    image, width=int(image.shape[1] / 2), height=int(image.shape[0] / 2)
)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
