"""
8. Efekty przy skalowaniu w górę
a. Powiększ obraz 4x używając INTER_CUBIC i INTER_LANCZOS4.
b. Porównaj ostrość obrazu w obu przypadkach.

"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized_cubic = imutils.resize(
    image,
    width=image.shape[1] * 4,
    height=image.shape[0] * 4,
    inter=cv2.INTER_CUBIC,
)

resized_lanczos4 = imutils.resize(
    image,
    width=image.shape[1] * 4,
    height=image.shape[0] * 4,
    inter=cv2.INTER_LANCZOS4,
)

cv2.imshow("Resized image - INTER_CUBIC", resized_cubic)
cv2.imshow("Resized image - INTER_LANCZOS4", resized_lanczos4)

cv2.waitKey(0)
cv2.destroyAllWindows()
