"""
3. Przycięcie prawej połowy obrazu
a. Przycięcie prawej połowy obrazu
b. Wyświetl tylko prawą połowę.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

height, width = image.shape[:2]

right_half = image[0:height, width // 2 : width]

cv2.imshow("Right half", right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
