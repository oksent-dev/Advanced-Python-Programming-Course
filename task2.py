"""
2. Eksperymentowanie z dylatacją
a. Pobierz obraz zawierający cienkie linie lub przerwy między obiektami.
b. Zastosuj dylatację z różnymi rozmiarami elementów strukturalnych.
c. Przedstaw wykres lub tabelę pokazującą, jak zmienia się grubość
obiektów w zależności od liczby iteracji dylatacji.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Loading images...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 231, 255, cv2.THRESH_BINARY_INV)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

iterations = [i for i in range(1, 5 + 1)]
thickness_square = []
thickness_ellipse = []

for i in iterations:
    image_dilation_square = cv2.dilate(image, kernel_square, iterations=i)
    thickness_square.append(np.sum(image_dilation_square == 255))

    image_dilation_ellipse = cv2.dilate(image, kernel_ellipse, iterations=i)
    thickness_ellipse.append(np.sum(image_dilation_ellipse == 255))

plt.figure(figsize=(10, 6))
plt.ylim(0, max(max(thickness_square), max(thickness_ellipse)) + 10000)
plt.xticks(iterations)
plt.plot(iterations, thickness_square, label="Square Kernel", linewidth=2)
plt.plot(iterations, thickness_ellipse, label="Ellipse Kernel", linewidth=2)
plt.title("Change in Object Thickness with Dilation Iterations")
plt.xlabel("Number of Iterations")
plt.ylabel("Thickness")
plt.legend()
plt.grid()
plt.show()
