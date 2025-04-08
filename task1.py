"""
1. Wstęp do progowania
a. Wczytaj wskazany obraz, przekształć go do skali szarości, a następnie
zastosuj progowanie podstawowe dla wartości progowej:
i. T = 30
ii. T = 100
iii. T = 200
b. Porównaj uzyskane binarne obrazy. Która wartość progowa najlepiej
oddziela pierwszy plan od tła? Jeśli żadna to spróbuj dobrać odpowiednią.

================================================================
b) Która wartość progowa najlepiej oddziela pierwszy plan od tła?
Wartość progowa T=150 idealnie oddziela pierwszy plan od tła.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresholds = [30, 100, 150, 200]
binary_images = [
    cv2.threshold(gray_image, t, 255, cv2.THRESH_BINARY)[1] for t in thresholds
]

plt.figure(figsize=(12, 10))
plt.subplot(3, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

for i, (t, binary) in enumerate(zip(thresholds, binary_images), start=2):
    plt.subplot(3, 2, i)
    plt.imshow(binary, cmap="gray")
    plt.title(f"Threshold T={t}")
    plt.axis("off")

plt.tight_layout()
plt.show()
