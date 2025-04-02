"""
4. Analiza wpływu rozmycia na tekst na obrazie
a. Znajdź lub przygotuj obraz zawierający tekst (np. logo, znak drogowy,
nagłówek gazety).
b. Zastosuj różne metody rozmycia (cv2.blur, cv2.GaussianBlur,
cv2.medianBlur, cv2.bilateralFilter) z różnymi parametrami.
c. Odpowiedz na pytania:
i. Które metody najmocniej rozmywają tekst?
ii. Które pozwalają zachować jego czytelność?

============================
i. Które metody najmocniej rozmywają tekst?
  - Rozmycie proste i rozmycie Gaussa najmocniej rozmywają tekst.
  - Przy wysokich wartościach kernela rozmycie medianowe również mocno rozmywa tekst.
ii. Które pozwalają zachować jego czytelność?
    - Rozmycie dwustronne najlepiej zachowuje czytelność tekstu
    - Rozmycie medianowe również dobrze zachowuje tekst, ale tylko przy niskich wartościach kernela.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Loading image...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

diameters = [5, 9, 15]
sigma_colors = [50, 75, 100]
sigma_spaces = [50, 75, 100]

fig, axes = plt.subplots(len(diameters), 4, figsize=(20, 15))
fig.suptitle("Comparison of Blurring Methods", fontsize=16)

for i, d in enumerate(diameters):
    bilateral_blur = cv2.bilateralFilter(image, d, sigma_colors[i], sigma_spaces[i])
    avg_blur = cv2.blur(image, (d, d))
    gauss_blur = cv2.GaussianBlur(image, (d, d), 0)
    median_blur = cv2.medianBlur(image, d)

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
