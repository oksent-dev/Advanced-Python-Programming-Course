"""
3. Eksperymentowanie z dużymi wartościami przesunięcia
a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
oryginalnego obrazu.
"""

import cv2
import numpy as np

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: cannot load image!")

(width, height) = (image.shape[1], image.shape[0])
M = np.float32([[1, 0, width // 2 + 50], [0, 1, height // 2 + 50]])
shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.namedWindow("Shifted image", cv2.WINDOW_NORMAL)
cv2.imshow("Shifted image", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
