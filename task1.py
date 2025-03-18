"""
1. Wybór ROI na podstawie współrzędnych
a. Zdefiniuj ROI, który obejmuje lewy górny róg obrazu o wymiarach 100x100
pikseli.
b. Wyświetl wynik.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

roi = image[0:100, 0:100]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
