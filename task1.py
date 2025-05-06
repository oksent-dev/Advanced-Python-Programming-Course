"""
1. Klasyczne progowanie
a. Wczytaj obraz z kostką brukową, przeskaluj go do szerokości 300 px i
zastosuj progowanie klasyczne ( cv2.threshold ) dla różnych wartości
progowania (np. 100, 140, 180).
b. Zaobserwuj, jak zmienia się jakość segmentacji kostek. Która wartość
progowania najlepiej rozdziela kostki od tła?

==========
Wartość progowania 140 wydaje się byćc najlepsza.
"""

import cv2
import matplotlib.pyplot as plt

print("Loading images...")
image = cv2.imread("kostka.png")

if image is None:
    print("Error: Image not found.")
    exit(0)

image_resized = cv2.resize(image, (300, int(image.shape[0] * 300 / image.shape[1])))
gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

thresholds = [100, 140, 180]
binary_images = [
    cv2.threshold(gray_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB))
plt.title("Original Image (Resized)")
plt.axis("off")

for i, (t, binary) in enumerate(zip(thresholds, binary_images), start=2):
    plt.subplot(2, 2, i)
    plt.imshow(binary, cmap="gray")
    plt.title(f"Threshold T={t}")
    plt.axis("off")

plt.tight_layout()
plt.show()
