"""
2. Wpływ rozmiaru sąsiedztwa
a. Na tym samym obrazie zastosuj cv2.adaptiveThreshold z różnymi wartościami
parametru blockSize : 11, 21, 31, 41
b. Który rozmiar najlepiej radzi sobie z detekcją konturów przy silnych
różnicach w oświetleniu?
===============================================
b) Który rozmiar najlepiej radzi sobie z detekcją konturów przy silnych różnicach w oświetleniu?
Najlepiej radzi sobie blockSize=21.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lighting.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

block_sizes = [11, 21, 31, 41]
adaptive_thresholds = [
    cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, 2
    )
    for block_size in block_sizes
]

plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

for i, (block_size, adaptive_thresh) in enumerate(
    zip(block_sizes, adaptive_thresholds), start=2
):
    plt.subplot(2, 3, i)
    plt.imshow(adaptive_thresh, cmap="gray")
    plt.title(f"Adaptive Threshold (blockSize={block_size})")
    plt.axis("off")

plt.tight_layout()
plt.show()
