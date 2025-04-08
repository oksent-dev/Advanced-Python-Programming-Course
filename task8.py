"""
8. Case study - kostka brukowa
a. Na obrazie kostki brukowej (może być z Internetu) zastosuj:
i. progowanie podstawowe z wybraną wartością T
ii. progowanie Otsu
b. Która metoda lepiej wykrywa wady powierzchni? Jak zmienia się wynik po
wygładzeniu i erozji?

====================================================
b) Która metoda lepiej wykrywa wady powierzchni? Jak zmienia się wynik po wygładzeniu i erozji?
Wynik progowania Otsu lepiej wykrywa wady powierzchni.
Po wygładzeniu i erozji wynik jest bardziej wyraźny, a szum został zredukowany.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("bricks.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_basic = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
_, binary_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, binary_otsu_blurred = cv2.threshold(
    blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

kernel = np.ones((3, 3), np.uint8)
eroded_image = cv2.erode(binary_otsu_blurred, kernel, iterations=1)

images = [
    (gray_image, "Original Grayscale Image"),
    (binary_basic, "Basic Threshold (T=100)"),
    (binary_otsu, "Otsu Threshold"),
    (blurred_image, "Blurred Grayscale Image"),
    (binary_otsu_blurred, "Otsu Threshold (Blurred)"),
    (eroded_image, "Eroded Image (After Otsu + Blur)"),
]

plt.figure(figsize=(12, 8))
for i, (img, title) in enumerate(images, start=1):
    plt.subplot(2, 3, i)
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
