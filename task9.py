"""
9. Obrót i zapis obrazu
a. Obróć obraz o 75 stopni i zapisz wynik do pliku rotated_output.jpg .
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

rotated = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)
print("Rotated image saved to 'rotated_output.jpg'")
