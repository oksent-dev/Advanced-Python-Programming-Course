"""
2. Odbicie pionowe
a. Wykonaj odbicie lustrzane w pionie.
b. Porównaj wynik z obrazem oryginalnym.
"""

import cv2


print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

cv2.imshow("original", image)

flipped = cv2.flip(image, 0)

cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
