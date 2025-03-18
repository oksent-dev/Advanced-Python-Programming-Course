"""
4. Porównanie efektów
a. Wyświetl cztery wersje obrazu:
i. Oryginał
ii. Odbicie poziome
iii. Odbicie pionowe
iv. Odbicie względem obu osi
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)

cv2.imshow("original", image)
cv2.imshow("flipped horizontal", flipped_horizontal)
cv2.imshow("flipped vertical", flipped_vertical)
cv2.imshow("flipped both", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
