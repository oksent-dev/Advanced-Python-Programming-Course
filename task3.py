"""
3. Obrót wokół narożnika
a. Obróć obraz o 30 stopni względem lewego górnego narożnika (0,0).
b. Wyświetl wynik.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
