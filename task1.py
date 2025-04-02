"""
1. Eksploracja różnych metod rozmycia
a. Załaduj dowolny obraz i zastosuj do niego cztery różne metody rozmycia
i. proste rozmycie cv2.blur
ii. rozmycie Gaussa cv2.GaussianBlur
iii. rozmycie medianowe cv2.medianBlur
iv. rozmycie dwustronne cv2.bilateralFilter
b. Dla każdej metody porównaj efekty wizualne przy różnych wartościach
parametrów kernela. Odpowiedz na pytania (w formie komentarza w
kodzie):
i. Która metoda najlepiej usuwa szum?
ii. Która metoda zachowuje najwięcej szczegółów?
iii. Jakie są zalety i wady każdej metody?
=================================
i. Szum najlepiej usuwa rozmycie Gaussa.
ii. Rozmycie dwustronne zachowuje najwięcej szczegółów.
iii. Zalety i wady każdej metody:
- Rozmycie proste:
    - Zalety:
        Szybkość obliczeniowa
    - Wady:
        Nie usuwa dobrze szumów
        Rozmazuje szczegóły
        Nie zachowuje krawędzi

- Rozmycie Gaussa:
        - Zalety:
            Dobrze usuwa szumy
        - Wady:
            Wolniejsze niż rozmycie proste

- Rozmycie medianowe:
        - Zalety:
            Usuwa szumy
            Zachowuje więcej szczegółów niż rozmycie proste
        - Wady:
            Wciąż zachowuje mniej szczegółów niż rozmycie dwustronne
            wolniejsze niż rozmycie proste

- Rozmycie dwustronne:
        - Zalety:
            Usuwa szumy
            Zachowuje najwięcej szczegółów
        - Wady:
            Najwolniejsze z wszystkich metod
            Wymaga więcej pamięci

"""

import cv2

print("Loading image...")
image = cv2.imread("example2.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

kernel = (13, 13)

blurred_image = cv2.blur(image, kernel)
gaussian_blurred_image = cv2.GaussianBlur(image, kernel, 0)
median_blurred_image = cv2.medianBlur(image, 13)
bilateral_blurred_image = cv2.bilateralFilter(image, 13, 75, 75)
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Gaussian Blurred Image", gaussian_blurred_image)
cv2.imshow("Median Blurred Image", median_blurred_image)
cv2.imshow("Bilateral Blurred Image", bilateral_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
