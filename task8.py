"""
8. Obrót sekwencyjny
a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
końcowy.
b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.

===
Zdecydowanie wynik różni się od pojedynczego obrotu o 90 stopni
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

rotated = imutils.rotate(image, 30)
for i in range(2):
    rotated = imutils.rotate(rotated, 30)

rotated_90 = imutils.rotate(image, 90)

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.namedWindow("Rotated 90", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated 90", rotated_90)

cv2.waitKey(0)
cv2.destroyAllWindows()
