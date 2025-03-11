"""
5. Eksperymentowanie z pętlą
a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
poprzedniego i mieć środek w tym samym miejscu.
"""

import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
for r in range(0, 150, 10):
    cv2.rectangle(canvas, (centerX - r, centerY - r), (centerX + r, centerY + r), white)

cv2.imshow("Squares", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
