"""
6. Odbicie na podstawie wyboru użytkownika
a. Napisz skrypt, który wczytuje obraz i pyta użytkownika o sposób odbicia
( 0 - pionowe, 1 - poziome, -1 - oba).
b. Na podstawie wyboru wykonuje operację i wyświetla wynik.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

option = int(input("Choose flip option (0 - vertical, 1 - horizontal, -1 - both): "))
flipped = cv2.flip(image, option)

cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
