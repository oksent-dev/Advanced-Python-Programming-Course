"""
9. Dynamiczna zmiana rozmiaru w pętli
a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co
20%.
b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem ( cv2.waitKey(500) ).
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

for i in range(20, 220, 20):
    resized = imutils.resize(image, width=image.shape[1] + i)
    cv2.imshow(f"Resized image - {100 + i}%", resized)
    cv2.waitKey(500)

cv2.destroyAllWindows()
