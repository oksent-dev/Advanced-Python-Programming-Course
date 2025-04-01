"""
1. Analiza wpływu erozji na obrazy
a. Wczytaj obraz binarny zawierający różne kształty (np. figury
geometryczne lub tekst).
b. Zastosuj operację erozji z różnymi elementami strukturalnymi (np.
kwadratowym i eliptycznym).
c. Opisz, jak zmienia się struktura obiektów w wyniku erozji.

====================================================================
W wyniku operacji erozji obiekty na obrazie stają się mniejsze,
podpisy pod obiektami znikneły a tytuł obrazu zwęził się.
"""

import cv2

print("Loading images...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 231, 255, cv2.THRESH_BINARY_INV)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

image_erosion_square = cv2.erode(image, kernel_square, iterations=1)
image_erosion_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Erosion with Square Kernel", image_erosion_square)
cv2.imshow("Erosion with Elliptical Kernel", image_erosion_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()
