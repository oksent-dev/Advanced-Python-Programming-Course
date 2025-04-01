"""
4. Łączenie przerw w obiektach za pomocą zamknięcia
a. Pobierz obraz zawierający znaki lub litery z przerwami w konturach.
b. Wykorzystaj zamknięcie do połączenia fragmentów znaków i poprawienia
ich czytelności.
c. Porównaj efekty różnych kształtów elementów strukturalnych (np.
prostokątnego, eliptycznego).
=================================================================
Prawie wszystkie kontury zostały połączone
"""

import cv2
import numpy as np

print("Loading images...")
image = cv2.imread("google.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 231, 255, cv2.THRESH_BINARY_INV)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))

image_closing_square = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_square)
image_closing_ellipse = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_ellipse)

cv2.imshow("Original Image", image)
cv2.imshow("Closing with Square Kernel", image_closing_square)
cv2.imshow("Closing with Elliptical Kernel", image_closing_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()
