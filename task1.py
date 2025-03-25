"""
1. Wyświetlenie pojedynczych kanałów na obrazie
a. Wczytaj dowolny obraz.
b. Rozdziel kanały B, G, R i wyświetl je osobno.
c. Zapisz te kanały jako osobne obrazy.
"""

import cv2

print("Loading images...")
image = cv2.imread("opencv_logo.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

b, g, r = cv2.split(image)

cv2.namedWindow("Red", cv2.WINDOW_NORMAL)
cv2.imshow("Red", r)
cv2.namedWindow("Green", cv2.WINDOW_NORMAL)
cv2.imshow("Green", g)
cv2.namedWindow("Blue", cv2.WINDOW_NORMAL)
cv2.imshow("Blue", b)

cv2.imwrite("red.jpg", r)
cv2.imwrite("green.jpg", g)
cv2.imwrite("blue.jpg", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
