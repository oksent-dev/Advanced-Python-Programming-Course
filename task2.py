"""
2. Rysowanie prostokątów, utwórz czarny obraz o wymiarach 400x400 pikseli i
narysuj na nim:
a. Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
b. Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.
"""

import numpy as np
import cv2

canvas = np.zeros((400, 400, 3), dtype="uint8")

cv2.rectangle(canvas, (0, 0), (100, 50), (0, 255, 0))
cv2.rectangle(canvas, (300, 350), (400, 400), (0, 0, 255), 3)
cv2.imshow("Rectangles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
