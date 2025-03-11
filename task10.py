"""
10. Obrót w pętli
a. Wykonaj pętlę, która obraca obraz co 15 stopni od 0 do 360 i wyświetla
każdą wersję na ekranie.
b. Dodaj opóźnienie cv2.waitKey(500) , aby obserwować zmiany.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

for i in range(0, 360, 15):
    rotated = imutils.rotate(image, i)
    cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(500)
