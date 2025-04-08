"""
6. Analiza histogramu
a. wygeneruj histogram skali szarości ( cv2.calcHist )
b. zaznacz na nim wartość progową wyliczoną przez Otsu
c. Czy na histogramie można wyraźnie dostrzec dwa zbiory intensywności
(tło vs obiekt)? Jak Otsu wybiera próg?

====================================================
b) Czy na histogramie można wyraźnie dostrzec dwa zbiory intensywności (tło vs obiekt)? Jak Otsu wybiera próg?
Tak, choć w tym przykładzie można rozróżnić trzy zbiory intensywności.
Otsu Wybiera próg, który najlepiej oddziela dwa zbiory intensywności, minimalizując nakładkę między nimi.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_threshold = _

hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.plot(hist, color="black")
plt.axvline(
    x=otsu_threshold,
    color="red",
    linestyle="--",
    label=f"Otsu Threshold = {otsu_threshold:.2f}",
)
plt.title("Histogram with Otsu Threshold")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()
