"""
6. Obrót bez przycinania ( rotate_bound )
a. Wykorzystaj imutils.rotate_bound , aby obrócić obraz o -33 stopnie i uniknąć
przycięcia.
b. Wyświetl wynik.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

rotated = imutils.rotate_bound(image, -33)

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
