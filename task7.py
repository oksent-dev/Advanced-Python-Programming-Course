"""
7. Analiza nasycenia w obrazie
a. Wczytaj dowolny obraz i przekonwertuj go do przestrzeni HSV.
b. Rozdziel obraz na kanały H, S i V.
c. Obniż poziom nasycenia (S) w całym obrazie.
d. Podwyższ poziom nasycenia (S) w całym obrazie.
e. Porównaj zmodyfikowane obrazy z oryginałem.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)

s_lowered = cv2.subtract(s, 50)
s_increased = cv2.add(s, 50)

image_hsv_lowered = cv2.merge((h, s_lowered, v))
image_hsv_increased = cv2.merge((h, s_increased, v))

image_rgb_original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgb_lowered = cv2.cvtColor(image_hsv_lowered, cv2.COLOR_HSV2RGB)
image_rgb_increased = cv2.cvtColor(image_hsv_increased, cv2.COLOR_HSV2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image_rgb_original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(image_rgb_lowered)
plt.title("Lowered Saturation")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(image_rgb_increased)
plt.title("Increased Saturation")
plt.axis("off")

plt.tight_layout()
plt.show()
