"""
2. Analiza cech uwidaczniających się w poszczególnych kanałach
a. Wybierz obraz, na którym znajdują się obiekty o różnych kolorach.
b. Porównaj, jak różne elementy obrazu są widoczne w poszczególnych
kanałach B, G, R.
c. Spróbuj znaleźć taki obiekt, który jest wyraźnie widoczny tylko na jednym
z kanałów.

===================
na każdym kanale widać tylko jeden półokrąg z loga
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

cv2.waitKey(0)
cv2.destroyAllWindows()
