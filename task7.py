"""
7. Podział obrazu na siatkę
a. Podziel obraz na 9 równych części (3x3).
b. Wyświetl wszystkie części osobno.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

height, width = image.shape[:2]

n = 3
for i in range(n):
    for j in range(n):
        part = image[
            i * height // n : (i + 1) * height // n,
            j * width // n : (j + 1) * width // n,
        ]
        cv2.imshow(f"Part {i * 3 + j + 1}", part)

cv2.waitKey(0)
cv2.destroyAllWindows()
