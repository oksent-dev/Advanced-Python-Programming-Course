"""
3. Odbicie względem obu osi
a. Odbij obraz zarówno poziomo, jak i pionowo (czyli względem obu osi).
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

flipped = cv2.flip(image, -1)

cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
