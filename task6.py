"""
6. Symulacja efektu głębi ostrości (dobrze znana fraza w fotografii, jeśli jej nie
znasz, to zrób research)
a. Wybierz zdjęcie z obiektami w różnych odległościach od aparatu.
b. Spróbuj zasymulować efekt głębi ostrości, rozmywając tylko tło, a
pozostawiając główny obiekt wyraźny.
c. Możesz zrobić to, ręcznie maskując obszar tła i stosując cv2.GaussianBlur
tylko na nim.
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("box.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)


mask = np.zeros(image.shape[:2], dtype="uint8")
x = 1
y = 347
w = 561
h = 430
cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

blurred_image = cv2.GaussianBlur(image, (23, 23), 0)

result = np.where(mask[:, :, None] == 255, image, blurred_image)

cv2.imshow("Original Image", image)
cv2.imshow("Depth of Field Effect", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
