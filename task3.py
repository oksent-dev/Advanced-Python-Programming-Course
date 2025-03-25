"""
3. Rekonstrukcja obrazu po manipulacji kanałami
a. Zamień wartości kanałów miejscami, np. wyświetl obraz w kolejności R, B,
G.
b. Ustaw wartość jednego z kanałów na zero i zobacz, jak zmienia się wygląd
obrazu.
"""

import cv2

print("Loading images...")
image = cv2.imread("opencv_logo.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

b, g, r = cv2.split(image)

image = cv2.merge((r, b, g))

image_without_blue = cv2.merge((0 * b, g, r))

cv2.namedWindow("Reconstructed", cv2.WINDOW_NORMAL)
cv2.imshow("Reconstructed", image)

cv2.namedWindow("Without blue", cv2.WINDOW_NORMAL)
cv2.imshow("Without blue", image_without_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
