"""
3. Wykorzystanie maski do ekstrakcji koloru
a. Wczytaj kolorowy obraz (np. kwiaty, samochód).
b. Stwórz maskę w taki sposób, aby pozostawić tylko jeden wybrany kolor, a
resztę obrazu zaciemnić.
c. Wskazówka: użyj konwersji obrazu do przestrzeni barw HSV i maskowania
na podstawie zakresu kolorów.
"""

import cv2
import numpy as np

print("Loading images...")
image = cv2.imread("red_car.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Masked image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
