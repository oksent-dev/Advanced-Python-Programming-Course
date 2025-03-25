"""
6. Eksperymentowanie z logiem OpenCV
a. Pobierz logo OpenCV i rozdziel jego kanały.
b. Spróbuj zamienić kolory tak, aby wyglądało inaczej, np. zamienić niebieski
z czerwonym.
c. Spróbuj usunąć jeden kanał całkowicie i sprawdź, jak wpłynie to na wygląd
loga.
"""

import cv2

print("Loading images...")
image = cv2.imread("opencv_logo.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

b, g, r = cv2.split(image)

image = cv2.merge((r, g * 0, b))

cv2.namedWindow("Reconstructed", cv2.WINDOW_NORMAL)
cv2.imshow("Reconstructed", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
