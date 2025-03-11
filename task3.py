"""
3. Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
narysuj na nim:
a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
b. Czerwony okrąg o promieniu 60 px w środku obrazu.
"""

import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

cv2.circle(canvas, (40, 40), 40, (255, 0, 0))
cv2.circle(canvas, (150, 150), 60, (0, 0, 255))
cv2.imshow("Circles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
