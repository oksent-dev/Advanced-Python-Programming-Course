"""
3. Rozmycie dwustronne w praktyce
a. Załaduj zdjęcie zawierające zarówno szum, jak i ostre krawędzie.
b. Zastosuj rozmycie dwustronne (cv2.bilateralFilter) z różnymi wartościami
parametrów.
c. Porównaj efekty z innymi metodami rozmycia.
d. Odpowiedz na pytania (w formie komentarza w kodzie):
i. Czy rozmycie dwustronne skutecznie redukuje szum?
ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
iii. Jakie wartości parametrów dają najlepsze rezultaty?
=========================
i. Czy rozmycie dwustronne skutecznie redukuje szum?
   - Tak, rozmycie dwustronne skutecznie redukuje szum, jednocześnie zachowując ostre krawędzie.

ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
   - Tak, rozmycie dwustronne zachowuje krawędzie lepiej niż inne metody.
   - Rozmycie medianowe również dobrze zachowuje krawędzie jednak mniejsze napisy stają się nieczytelne.

iii. Jakie wartości parametrów dają najlepsze rezultaty?
   - Najlepsze rezultaty zależą od obrazu i poziomu szumu.
   W tym przypadku wartości `d=15`, `sigmaColor=100`, `sigmaSpace=100` dają dobre efekty, redukując szum i zachowując krawędzie.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy = image.copy()
    total_pixels = image.size

    num_salt = int(total_pixels * salt_prob)
    coords = [np.random.randint(0, i, num_salt) for i in image.shape]
    noisy[coords[0], coords[1]] = 255

    num_pepper = int(total_pixels * pepper_prob)
    coords = [np.random.randint(0, i, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy


print("Loading image...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

noisy_image = salt_and_pepper_noise(image, 0.02, 0.02)

diameters = [5, 9, 15]
sigma_colors = [50, 75, 100]
sigma_spaces = [50, 75, 100]

fig, axes = plt.subplots(len(diameters), 4, figsize=(20, 15))
fig.suptitle("Comparison of Blurring Methods with Noisy Image", fontsize=16)

for i, d in enumerate(diameters):
    bilateral_blur = cv2.bilateralFilter(
        noisy_image, d, sigma_colors[i], sigma_spaces[i]
    )
    avg_blur = cv2.blur(noisy_image, (d, d))
    gauss_blur = cv2.GaussianBlur(noisy_image, (d, d), 0)
    median_blur = cv2.medianBlur(noisy_image, d)

    axes[i, 0].imshow(avg_blur, cmap="gray")
    axes[i, 0].set_title(f"Average Blur d={d}")
    axes[i, 0].axis("off")

    axes[i, 1].imshow(gauss_blur, cmap="gray")
    axes[i, 1].set_title(f"Gaussian Blur d={d}")
    axes[i, 1].axis("off")

    axes[i, 2].imshow(median_blur, cmap="gray")
    axes[i, 2].set_title(f"Median Blur d={d}")
    axes[i, 2].axis("off")

    axes[i, 3].imshow(bilateral_blur, cmap="gray")
    axes[i, 3].set_title(f"Bilateral Blur d={d}")
    axes[i, 3].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
