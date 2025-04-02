"""
2. Analiza wpływu rozmiaru kernela na efekt rozmycia
a. Zastosuj każdą z metod rozmycia do obrazu, używając różnych wartości
kernela: (3x3), (5x5), (9x9), (15x15).
b. Porównaj wyniki i odpowiedz na pytania (w formie komentarza w kodzie):
i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty
istotnych detali?
============================
i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
   - Im większy kernel, tym bardziej obraz staje się rozmyty. Detale są coraz bardziej tracone, a krawędzie stają się mniej wyraźne.
   - Rozmycie dwustronne zachowuje krawędzie lepiej niż inne metody, nawet przy większych rozmiarach kernela.

ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
   - Optymalny rozmiar kernela zależy od obrazu i poziomu szumu.
     Dla większości przypadków w tym obrazie kernel (5x5) lub (9x9) dobrze redukuje szum, zachowując istotne detale.
"""

import cv2
import matplotlib.pyplot as plt

print("Loading image...")
image = cv2.imread("example2.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

# Convert to grayscale for simplicity
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define kernel sizes
kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

# Prepare subplots
fig, axes = plt.subplots(len(kernel_sizes), 4, figsize=(20, 10))
fig.suptitle("Effect of Kernel Size on Blurring Methods", fontsize=16)

for i, kernel_size in enumerate(kernel_sizes):
    avg_blur = cv2.blur(gray_image, kernel_size)
    gauss_blur = cv2.GaussianBlur(gray_image, kernel_size, 0)
    median_blur = cv2.medianBlur(gray_image, kernel_size[0])
    bilateral_blur = cv2.bilateralFilter(gray_image, kernel_size[0], 75, 75)

    axes[i, 0].imshow(avg_blur, cmap="gray")
    axes[i, 0].set_title(f"Average Blur {kernel_size}")
    axes[i, 0].axis("off")

    axes[i, 1].imshow(gauss_blur, cmap="gray")
    axes[i, 1].set_title(f"Gaussian Blur {kernel_size}")
    axes[i, 1].axis("off")

    axes[i, 2].imshow(median_blur, cmap="gray")
    axes[i, 2].set_title(f"Median Blur {kernel_size}")
    axes[i, 2].axis("off")

    axes[i, 3].imshow(bilateral_blur, cmap="gray")
    axes[i, 3].set_title(f"Bilateral Blur {kernel_size}")
    axes[i, 3].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
