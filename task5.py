"""
5. Porównanie skuteczności redukcji szumów
a. Dodaj do obrazu sztuczny szum soli i pieprzu (za pomocą cv2.randu).
b. Następnie zastosuj różne metody rozmycia i oceń, która najlepiej usuwa
szum, zachowując detale obrazu.
=============================
1. Która metoda najlepiej usuwa szum, zachowując detale obrazu?
   - Rozmycie medianowe
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Loading image...")
image = cv2.imread("example2.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy = image.copy()
    random_matrix = np.zeros_like(image, dtype=np.float32)
    cv2.randu(random_matrix, 0, 1)
    noisy[random_matrix < salt_prob] = 255
    noisy[random_matrix > 1 - pepper_prob] = 0
    return noisy


noisy_image_sp = salt_and_pepper_noise(gray_image, 0.02, 0.02)

kernel_size = (5, 5)

avg_blur_sp = cv2.blur(noisy_image_sp, kernel_size)
gauss_blur_sp = cv2.GaussianBlur(noisy_image_sp, kernel_size, 0)
median_blur_sp = cv2.medianBlur(noisy_image_sp, kernel_size[0])
bilateral_blur_sp = cv2.bilateralFilter(noisy_image_sp, kernel_size[0], 75, 75)

fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.suptitle("Noise Reduction Comparison", fontsize=16)

axes[0, 0].imshow(gray_image, cmap="gray")
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")

axes[0, 1].imshow(noisy_image_sp, cmap="gray")
axes[0, 1].set_title("Salt & Pepper Noise")
axes[0, 1].axis("off")

axes[0, 2].axis("off")
axes[0, 3].axis("off")

axes[1, 0].imshow(avg_blur_sp, cmap="gray")
axes[1, 0].set_title("Avg Blur")
axes[1, 0].axis("off")

axes[1, 1].imshow(gauss_blur_sp, cmap="gray")
axes[1, 1].set_title("Gaussian Blur")
axes[1, 1].axis("off")

axes[1, 2].imshow(median_blur_sp, cmap="gray")
axes[1, 2].set_title("Median Blur")
axes[1, 2].axis("off")

axes[1, 3].imshow(bilateral_blur_sp, cmap="gray")
axes[1, 3].set_title("Bilateral Blur")
axes[1, 3].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
