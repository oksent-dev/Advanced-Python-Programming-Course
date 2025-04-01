"""
5. Eksperymentowanie z różnymi elementami strukturalnymi
a. Wybierz jeden obraz testowy i wykonaj na nim wszystkie podstawowe
operacje morfologiczne (erozja, dylatacja, otwarcie, zamknięcie, gradient).
b. Powtórz eksperyment, zmieniając kształt elementu strukturalnego (np.
kwadrat, krzyż, elipsa).
c. Porównaj wyniki i opisz, jakie różnice zauważasz w przetworzonych
obrazach.
====================================================================
Na obrazie zostały kontury figur, które są bardziej wyraźne.
W przypadku elementu strukturalnego w kształcie prostokąta kontury są grubsze
niż w przypadku elementu w kształcie elipsy.
"""

import cv2


def apply_morphological_operations(image, kernel):
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    return image


print("Loading images...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 231, 255, cv2.THRESH_BINARY_INV)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

image_square = apply_morphological_operations(image, kernel_square)
image_ellipse = apply_morphological_operations(image, kernel_ellipse)

cv2.imshow("Original Image", image)
cv2.imshow("Morphological Operations with Square Kernel", image_square)
cv2.imshow("Morphological Operations with Elliptical Kernel", image_ellipse)

cv2.waitKey(0)
cv2.destroyAllWindows()
