"""
3. Różne metody adaptacyjne
a. Zastosuj dwie metody:
i. cv2.ADAPTIVE_THRESH_MEAN_C
ii. cv2.ADAPTIVE_THRESH_GAUSSIAN_C
b. Dla każdej z nich przetestuj różne wartości C (np. 2, 5, 10, 15).
c. Która metoda i jaki parametr C lepiej radzi sobie z szumem i nierównym
tłem?
==============================================
c) Która metoda i jaki parametr C lepiej radzi sobie z szumem i nierównym tłem?
Najlepszy jest parametr C=2 gdyż inne usuwają szczegóły. cv2.ADAPTIVE_GAUSSIAN_C
lepiej radzi sobie z szumem.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lighting.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

C_values = [2, 5, 10, 15]
adaptive_mean = [
    cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, C
    )
    for C in C_values
]
adaptive_gaussian = [
    cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, C
    )
    for C in C_values
]

plt.figure(figsize=(12, 12))
for i, (C, mean_thresh, gauss_thresh) in enumerate(
    zip(C_values, adaptive_mean, adaptive_gaussian), start=1
):
    plt.subplot(4, 2, 2 * i - 1)
    plt.imshow(mean_thresh, cmap="gray")
    plt.title(f"Adaptive Mean (C={C})")
    plt.axis("off")

    plt.subplot(4, 2, 2 * i)
    plt.imshow(gauss_thresh, cmap="gray")
    plt.title(f"Adaptive Gaussian (C={C})")
    plt.axis("off")

plt.tight_layout()
plt.show()
