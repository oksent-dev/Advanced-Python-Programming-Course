"""
2. Wpływ rozmycia
a. Do jednego z obrazów z Zadania 1 zastosuj rozmycie Gaussa
( cv2.GaussianBlur ) przed progowaniem.
b. Porównaj wynik progowania z i bez rozmycia. Jak rozmycie wpływa na
jakość binarnego obrazu?
==========================================================
b) jak rozmycie wpływa na jakość binarnego obrazu?
Po zastosowaniu rozmycia Gaussa jakość binarnego obrazu poprawia się.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (25, 25), 0)

thresholds = [100, 150]
binary_images_original = [
    cv2.threshold(gray_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]
binary_images_blurred = [
    cv2.threshold(blurred_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]

plt.figure(figsize=(12, 8))
plt.subplot(3, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(3, 2, 2)
plt.imshow(blurred_image, cmap="gray")
plt.title("Blurred Grayscale Image")
plt.axis("off")

for i, (t, binary) in enumerate(zip(thresholds, binary_images_original), start=3):
    plt.subplot(3, 2, i)
    plt.imshow(binary, cmap="gray")
    plt.title(f"Original Threshold T={t}")
    plt.axis("off")

for i, (t, binary) in enumerate(zip(thresholds, binary_images_blurred), start=5):
    plt.subplot(3, 2, i)
    plt.imshow(binary, cmap="gray")
    plt.title(f"Blurred Threshold T={t}")
    plt.axis("off")

plt.tight_layout()
plt.show()
