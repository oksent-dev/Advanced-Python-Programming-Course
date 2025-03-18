"""
5. Automatyczne skalowanie na podstawie szerokości
a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
b. Użyj imutils.resize() .
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
resized_cv2 = cv2.resize(image, dim)
cv2.imshow("Resized image cv2", resized_cv2)

resized_imutils = imutils.resize(image, width=500)
cv2.imshow("Resized image imutils", resized_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()
