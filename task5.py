"""
5. Wykrywanie zielonych obiektów w przestrzeni HSV
a. Wczytaj obraz, który zawiera zarówno zielone obiekty, jak i inne kolory.
b. Przekonwertuj obraz do przestrzeni HSV.
c. Ustaw przedział wartości dla koloru zielonego w HSV.
d. Wygeneruj maskę zaznaczającą tylko zielone elementy.
e. Nałóż maskę na oryginalny obraz i wyświetl wynik.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("opencv_logo.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = (40, 50, 50)
upper_green = (80, 255, 255)

mask = cv2.inRange(image_hsv, lower_green, upper_green)
result = cv2.bitwise_and(image, image, mask=mask)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Green Object Detection")
plt.axis("off")

plt.tight_layout()
plt.show()
