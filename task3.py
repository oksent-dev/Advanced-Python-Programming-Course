"""
3. Wykrywanie niebieskich obiektów w przestrzeni HSV
a. Znajdź i wczytaj obraz zawierający wyraźny niebieski element.
b. Przekonwertuj obraz do przestrzeni HSV.
c. Zdefiniuj zakres wartości H, S i V odpowiadających kolorowi niebieskiemu.
d. Stwórz maskę, która zaznaczy obiekty w tym zakresie kolorów.
e. Nałóż maskę na oryginalny obraz i wyświetl efekt segmentacji.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("opencv_logo.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = (100, 150, 50)
upper_blue = (140, 255, 255)

mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
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
plt.title("Blue Object Detection")
plt.axis("off")

plt.tight_layout()
plt.show()
