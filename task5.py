"""
5. Obrót o 180 stopni za pomocą imutils.rotate
a. Skorzystaj z imutils.rotate , aby obrócić obraz o 180 stopni.
b. Wyświetl wynik.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

rotated = imutils.rotate(image, 180)

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
