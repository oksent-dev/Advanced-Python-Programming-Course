"""
4. Tworzenie własnego "filtra Instagram":
a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego
+10.
b. Sprawdź, jak zmienia się obraz.
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

M = np.ones(image.shape, dtype="uint8")
M[:, :, 0] += 30
M[:, :, 1] += 0
M[:, :, 2] += 10

M2 = np.ones(image.shape, dtype="uint8")
M2[:, :, 1] += 20


filtered = cv2.add(image, M)
filtered = cv2.subtract(filtered, M2)

cv2.imshow("Filtered", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
