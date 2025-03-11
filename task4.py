"""
4. Obrót o dowolny kąt
a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
b. Wyświetl wynik.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

angle = float(input("Enter the angle of rotation: "))

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
