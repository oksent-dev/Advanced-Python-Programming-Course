"""
1. Wizualizacja składowych RGB i HSV
a. Wybierz dowolny obraz (najlepiej z wyraźnymi kolorami) i wczytaj go do
programu.
b. Przekonwertuj obraz do przestrzeni RGB i wyświetl go.
c. Rozdziel obraz na trzy kanały (R, G, B) i wyświetl je osobno.
d. Przekonwertuj obraz do przestrzeni HSV i wyświetl go.
e. Rozdziel obraz na trzy kanały (H, S, V) i wyświetl je osobno.
f. Porównaj wpływ poszczególnych kanałów na wygląd obrazu.
"""

import cv2
import matplotlib.pyplot as plt

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image_rgb)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)

images = [
    (image_rgb, "Original Image (RGB)", None),
    (r, "Red Channel", "Reds"),
    (g, "Green Channel", "Greens"),
    (b, "Blue Channel", "Blues"),
    (cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB), "Original Image (HSV)", None),
    (h, "Hue Channel", "hsv"),
    (s, "Saturation Channel", "gray"),
    (v, "Value Channel", "gray"),
]

plt.figure(figsize=(12, 8))
for i, (img, title, cmap) in enumerate(images, 1):
    plt.subplot(3, 3, i)
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
