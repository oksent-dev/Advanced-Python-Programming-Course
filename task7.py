"""
7. Maska i segmentacja
a. Zastosuj metodę Otsu, a następnie wykorzystaj uzyskaną binarną maskę
do „wycięcia” obiektu z oryginalnego obrazu ( cv2.bitwise_and ).
b. Czy obiekt został skutecznie oddzielony od tła? Jakie ograniczenia tej
metody można zauważyć?

===================================================
b) Czy obiekt został skutecznie oddzielony od tła? Jakie ograniczenia tej
metody można zauważyć?

Tak, obiekt został skutecznie oddzielony od tła. Prawdopodbnym ograniczeniem tej metody jest
to, że może nie działać dobrze w przypadku obrazów z wieloma obiektami o podobnych
intensywnościach, gdyż Otsu wybiera tylko jeden próg oddzielający dwa zbiory intensywności.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

masked_image = cv2.bitwise_and(image, image, mask=binary_otsu)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary_otsu, cmap="gray")
plt.title("Otsu Binary Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB))
plt.title("Segmented Object")
plt.axis("off")

plt.tight_layout()
plt.show()
