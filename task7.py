"""
7. Porównanie warpAffine i imutils.rotate
a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
imutils.rotate .
b. Porównaj wyniki i zwróć uwagę na różnice.

===
Nie zauważyłem różnic w wynikach.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))
rotated_imutils = imutils.rotate(image, 60)

cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", rotated)

cv2.namedWindow("Rotated imutils", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated imutils", rotated_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()
