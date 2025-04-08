"""
6. Rozpoznawanie koloru skóry w przestrzeni HSV
a. Wybierz zdjęcie przedstawiające osobę (portret lub zdjęcie całej sylwetki).
b. Przekonwertuj obraz do przestrzeni HSV.
c. Ustal zakres wartości HSV odpowiadający odcieniom skóry.
d. Wygeneruj maskę wykrywającą obszary skóry.
e. Wyświetl oryginalny obraz oraz efekt maskowania.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("woman.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_skin = (0, 20, 70)
upper_skin = (20, 255, 255)

mask = cv2.inRange(image_hsv, lower_skin, upper_skin)
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
plt.title("Skin Detection")
plt.axis("off")

plt.tight_layout()
plt.show()
