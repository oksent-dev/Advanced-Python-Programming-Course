"""
1. Obrót o 45 stopni
a. Wczytaj obraz i wykonaj obrót o 45 stopni wokół jego środka.
b. Wyświetl obraz przed i po rotacji.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", image)

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
