"""
5. Kadrowanie twarzy
a. Znajdź zdjęcie z twarzą.
b. Znajdź obszar, w którym się znajduje, i przytnij obraz tak, aby pozostała
tylko twarz.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

roi = image[0:300, 150:400]

cv2.imshow("Face", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
