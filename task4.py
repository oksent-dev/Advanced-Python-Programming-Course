"""
4. Segmentacja tekstu w dokumencie
a. Wczytaj obraz dokumentu (np. zdjęcie notatki z telefonu). Zastosuj
progowanie adaptacyjne, aby wyodrębnić tekst.
b. Wyświetl binarny obraz, na którym tekst będzie dobrze widoczny, nawet
jeśli oryginał jest nierówno doświetlony.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("notes.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

binary_adaptive_mean = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 10
)
binary_adaptive_gaussian = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10
)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary_adaptive_mean, cmap="gray")
plt.title("Adaptive Threshold (Mean)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(binary_adaptive_gaussian, cmap="gray")
plt.title("Adaptive Threshold (Gaussian)")
plt.axis("off")

plt.tight_layout()
plt.show()
