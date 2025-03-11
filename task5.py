"""
5. Dynamiczne przesunięcie na podstawie parametrów użytkownika
a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
b. Sprawdź, jak działa przesunięcie dla różnych wartości.
"""

import cv2
import numpy as np
import imutils

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: cannot load image!")

tx = int(input("Podaj wartość przesunięcia w poziomie: "))
ty = int(input("Podaj wartość przesunięcia w pionie: "))

shifted_image = imutils.translate(image, tx, ty)

cv2.namedWindow("Shifted image", cv2.WINDOW_NORMAL)
cv2.imshow("Shifted image", shifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
