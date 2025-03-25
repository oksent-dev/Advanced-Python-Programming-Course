"""
4. Wzmocnienie jednego z kanałów
a. Zwiększ intensywność jednego z kanałów (np. kanału czerwonego) i
zaobserwuj, jak wpływa to na końcowy wygląd obrazu.
b. Możesz to zrobić poprzez dodanie stałej wartości do danego kanału, np. R
= cv2.add(R, 50) .

===================
obraz zrobił się bardziej czerwony
"""

import cv2

print("Loading images...")
image = cv2.imread("example.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

b, g, r = cv2.split(image)
r = cv2.add(r, 50)

image = cv2.merge((b, g, r))

cv2.namedWindow("Reconstructed", cv2.WINDOW_NORMAL)
cv2.imshow("Reconstructed", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
