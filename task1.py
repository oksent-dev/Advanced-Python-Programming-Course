"""
1. Odbicie poziome
a. Wczytaj obraz i wykonaj odbicie lustrzane w poziomie.
b. Wyświetl wynik.
"""

import cv2


print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

flipped = cv2.flip(image, 1)

cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
