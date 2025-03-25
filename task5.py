"""
5. Zastosowanie maski do selektywnej modyfikacji kanałów
a. czytaj obraz i stwórz maskę obejmującą tylko wybrany obiekt (np.
czerwony samochód).
b. Wykorzystując maskę, zwiększ nasycenie koloru czerwonego tylko w tej
części obrazu.

"""

#  (20, 100), (800, 500)

import cv2
import numpy as np

print("Loading images...")
image = cv2.imread("red_car.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

mask = np.ones(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (20, 100), (800, 500), 255, -1)

b, g, r = cv2.split(image)

r = cv2.add(r, 50, dst=r, mask=mask)

image = cv2.merge((b, g, r))

cv2.namedWindow("Reconstructed", cv2.WINDOW_NORMAL)
cv2.imshow("Reconstructed", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
