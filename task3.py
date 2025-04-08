"""
3. Efekty erozji
a. Do jednego z uzyskanych obrazów binarnych z Zadania 2 zastosuj
operację erozji ( cv2.erode ).
b. Opisz, jak zmienił się obraz po tej operacji. Czy zauważyłeś redukcję
szumów lub niechcianych pikseli?

=========================================================
b) Czy zauważyłeś redukcję szumów lub niechcianych pikseli?
Na obrazie nie było szumu, więc jedyną zmianą było ucięcie rogów ostrosłupa.
Jest to jednak dobra metoda do redukcji szumów i niechcianych pikseli.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

kernel = np.ones((15, 15), np.uint8)
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(binary_image, cmap="gray")
plt.title("Original Binary Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(eroded_image, cmap="gray")
plt.title("Eroded Image")
plt.axis("off")

plt.tight_layout()
plt.show()
