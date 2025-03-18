"""
3. Zmiana rozmiaru na konkretną wartość
a. Zmień rozmiar obrazu na dokładnie 200x300 pikseli.
b. Użyj cv2.resize().
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized = cv2.resize(image, (200, 300))
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
