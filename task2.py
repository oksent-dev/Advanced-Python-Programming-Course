"""
2. Modyfikacja jednego kanału i wpływ na obraz
a. Wczytaj obraz do programu i przekonwertuj go do przestrzeni HSV.
b. Rozdziel obraz na kanały H, S, V.
c. Wybierz jeden kanał (np. S - nasycenie) i zwiększ jego wartości o
określoną liczbę (np. +30).
d. Połącz kanały z powrotem i przekonwertuj obraz do przestrzeni RGB.
e. Wyświetl zmodyfikowany obraz i porównaj go z oryginałem.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)

s = cv2.add(s, 30)
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
plt.title("Modified Image (Saturation +30)")
plt.axis("off")

plt.tight_layout()
plt.show()
