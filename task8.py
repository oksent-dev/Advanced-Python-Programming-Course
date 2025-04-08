"""
8. Segmentacja kolorów z wieloma maskami
a. Wczytaj obraz zawierający elementy w różnych kolorach (np. niebieski,
czerwony, zielony).
b. Przekonwertuj obraz do przestrzeni HSV.
c. Utwórz oddzielne maski dla każdego koloru.
d. Połącz maski, aby wykryć wiele kolorów jednocześnie.
e. Wyświetl efekt segmentacji.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = (100, 150, 50)
upper_blue = (140, 255, 255)

lower_green = (40, 50, 50)
upper_green = (80, 255, 255)

lower_red1 = (0, 50, 50)
upper_red1 = (10, 255, 255)
lower_red2 = (170, 50, 50)
upper_red2 = (180, 255, 255)

mask_blue = cv2.inRange(image_hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(image_hsv, lower_green, upper_green)
mask_red1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(image_hsv, lower_red2, upper_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

combined_mask = cv2.bitwise_or(mask_blue, cv2.bitwise_or(mask_green, mask_red))

result = cv2.bitwise_and(image, image, mask=combined_mask)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Segmented Colors (Blue, Green, Red)")
plt.axis("off")

plt.tight_layout()
plt.show()
