"""
4. Wykorzystanie funkcji imutils.translate
a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
imutils.translate .
b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
Czy zauważyłeś różnice?
==========
Nie zauważyłem różnic.
"""

import cv2
import numpy as np
import imutils

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: cannot load image!")

shifted_image = imutils.translate(image, 100, 50)


cv2.namedWindow("Shifted image", cv2.WINDOW_NORMAL)
cv2.imshow("Shifted image", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
