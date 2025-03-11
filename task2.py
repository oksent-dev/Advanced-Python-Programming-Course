"""
2. Obrót o -90 stopni
a. Wczytaj obraz i obróć go o -90 stopni wokół środka.
b. Wyświetl wynik.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
