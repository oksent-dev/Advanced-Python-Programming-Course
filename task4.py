"""
4. Porównanie różnych metod interpolacji
a. Powiększ obraz 3x przy użyciu różnych metod interpolacji ( INTER_NEAREST ,
INTER_LINEAR , INTER_CUBIC , INTER_LANCZOS4 ).
"""

import cv2
import imutils

methods = [
    cv2.INTER_NEAREST,
    cv2.INTER_LINEAR,
    cv2.INTER_CUBIC,
    cv2.INTER_LANCZOS4,
]

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

for method in methods:
    resized = imutils.resize(
        image,
        width=int(image.shape[1] * 3),
        height=int(image.shape[0] * 3),
        inter=method,
    )
    cv2.imshow(f"Resized image ({method})", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
