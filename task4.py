"""
4. Wpływ oświetlenia
a. Zwiększ jasność obrazu o wartość 50 (np. dodając +50 do każdego
piksela w skali szarości).
b. Zastosuj podstawowe progowanie (np. T = 100) na obrazie oryginalnym i
rozjaśnionym. Jak zmienia się wynik? Co to mówi o czułości tej metody?
===================================================
b) Co to mówi o czułości tej metody?
Rozjaśnienie obrazu powoduje zmniejszenie czułości metody progowania.
Efektem jest nieprawidłowo wyodrębniony pierwszy plan.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

brightened_image = cv2.add(gray_image, 50)

thresholds = [150]
binary_images_original = [
    cv2.threshold(gray_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]
binary_images_brightened = [
    cv2.threshold(brightened_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]

images = [
    (gray_image, "Original Grayscale Image"),
    (brightened_image, "Brightened Grayscale Image (+50)"),
    *[
        (binary, f"Threshold T={t} (Original)")
        for t, binary in zip(thresholds, binary_images_original)
    ],
    *[
        (binary, f"Threshold T={t} (Brightened)")
        for t, binary in zip(thresholds, binary_images_brightened)
    ],
]

plt.figure(figsize=(12, 8))
for i, (img, title) in enumerate(images, start=1):
    plt.subplot(2, 2, i)
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
