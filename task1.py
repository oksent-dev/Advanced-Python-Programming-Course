"""
1. Podstawowe przesunięcie
a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy
transformacji M oraz cv2.warpAffine.
c. Wyświetl wynik.
"""

import cv2
import numpy as np

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: cannot load image!")

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow("Original image", image)
cv2.namedWindow("Shifted image", cv2.WINDOW_NORMAL)
cv2.imshow("Shifted image", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
