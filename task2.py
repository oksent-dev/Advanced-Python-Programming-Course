"""
2. Ukrywanie określonego obszaru twarzy
a. Wczytaj zdjęcie osoby.
b. Stwórz maskę zasłaniającą oczy (np. prostokąt lub elipsa).
c. Zastosuj maskę na obrazie i wyświetl wynik.
"""

import cv2
import numpy as np

print("Loading images...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

mask = np.ones(image.shape[:2], dtype="uint8") * 255

cv2.rectangle(mask, (250, 140), (380, 170), 0, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Masked image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
