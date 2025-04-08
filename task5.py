"""
5. Progowanie metodą Otsu
a. Zastosuj progowanie metodą Otsu do rozjaśnionego obrazu z Zadania 4.
b. Jak wygląda wynik? Porównaj go z wynikami z poprzedniego zadania. Co
mówi to o zaletach Otsu?
===================================================
b) Co mówi to o zaletach Otsu?
Czułość nie zmniejszyła sie po rozjaśnieniu obrazu. Otsu jest bardziej odporny na zmiany
oświetlenia niż podstawowe progowanie.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

brightened_image = cv2.add(gray_image, 50)

_, binary_otsu_original = cv2.threshold(
    gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
_, binary_otsu_brightened = cv2.threshold(
    brightened_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

images = [
    (gray_image, "Original Grayscale Image"),
    (brightened_image, "Brightened Grayscale Image (+50)"),
    (binary_otsu_original, "Otsu Threshold (Original)"),
    (binary_otsu_brightened, "Otsu Threshold (Brightened)"),
]

plt.figure(figsize=(12, 8))
for i, (img, title) in enumerate(images, start=1):
    plt.subplot(2, 2, i)
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
