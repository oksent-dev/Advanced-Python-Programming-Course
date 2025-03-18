"""
2. Przycięcie dolnej połowy obrazu
a. Podziel obraz na dwie równe części (górną i dolną).
b. Wyświetl tylko dolną połowę.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

height, width = image.shape[:2]

lower_half = image[height // 2 : height, 0:width]

cv2.imshow("Lower half", lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
