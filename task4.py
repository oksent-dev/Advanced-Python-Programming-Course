"""
4. Złożona figura
a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
Wszystko powinno być wycentrowane na obrazie.
"""

import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

cv2.rectangle(canvas, (100, 100), (200, 200), (255, 0, 0))
cv2.circle(canvas, (150, 150), 30, (0, 0, 255))
cv2.imshow("Complex figure", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
