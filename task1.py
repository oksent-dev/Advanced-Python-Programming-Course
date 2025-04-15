"""
1. Porównanie metod progowania
a. Wczytaj obraz z nierównym oświetleniem (np. kostka brukowa). Zastosuj
trzy metody progowania:
i. proste progowanie (wartość T=100),
ii. Otsu
iii. progowanie adaptacyjne (Mean i Gaussian).
b. Porównaj wyniki. Która metoda najlepiej poradziła sobie z nierównym
światłem?
==================================================================
b) Która metoda najlepiej poradziła sobie z nierównym światłem?
Zdecydowanie progrowanie adaptacyjne poradziło sobie najlepiej.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lighting.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_simple = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
_, binary_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
binary_adaptive_mean = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
binary_adaptive_gaussian = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

images = [
    (gray_image, "Original Grayscale Image"),
    (binary_simple, "Simple Threshold (T=100)"),
    (binary_otsu, "Otsu Threshold"),
    (binary_adaptive_mean, "Adaptive Threshold (Mean)"),
    (binary_adaptive_gaussian, "Adaptive Threshold (Gaussian)"),
]

plt.figure(figsize=(12, 8))
for i, (img, title) in enumerate(images, start=1):
    plt.subplot(2, 3, i)
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
