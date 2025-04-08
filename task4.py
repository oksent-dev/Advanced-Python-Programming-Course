"""
4. Manipulacja barwy obrazu (zmiana odcienia H)
a. Wczytaj obraz i przekonwertuj go do przestrzeni HSV.
b. Zwiększ wartość kanału H o określoną liczbę (np. +30), aby przesunąć
odcień kolorów.
c. Połącz zmodyfikowany obraz i przekonwertuj go z powrotem do
przestrzeni RGB.
d. Wyświetl obraz przed i po zmianie odcienia.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)

h = cv2.add(h, 30)
image_hsv_modified = cv2.merge((h, s, v))
image_rgb_modified = cv2.cvtColor(image_hsv_modified, cv2.COLOR_HSV2RGB)
image_rgb_original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb_original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(image_rgb_modified)
plt.title("Modified Image (Hue +30)")
plt.axis("off")

plt.tight_layout()
plt.show()
