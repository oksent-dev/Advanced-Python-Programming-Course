"""
6. Przygotowanie własnego przykładu zastosowania operacji morfologicznych
a. Wybierz realny przypadek użycia (np. poprawa czytelności tablic
rejestracyjnych, usuwanie szumu z dokumentów zeskanowanych, analiza obrazów medycznych).
b. Zastosuj odpowiednie operacje morfologiczne i zaprezentuj ich wpływ na
poprawę jakości analizy obrazu.

==========================================================
numery tablicy rejestracyjnej są bardziej wyraźne, a kontury są grubsze.
"""

import cv2

print("Loading images...")
image = cv2.imread("plate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

image_dilation_square = cv2.dilate(image, kernel_square, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Dilation with Square Kernel", image_dilation_square)
cv2.waitKey(0)
cv2.destroyAllWindows()
