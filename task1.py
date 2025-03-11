"""
1. Rysowanie linii
a. Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu.
Grubość linii: 2 px.
"""

import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

cv2.line(canvas, (150, 150), (300, 300), (255, 0, 0), 2)
cv2.imshow("Line", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
