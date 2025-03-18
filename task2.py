"""
2. Powiększenie obrazu dwukrotnie
a. Powiększ obraz 2x zarówno w pionie, jak i w poziomie.
b. Użyj metody cv2.INTER_LINEAR .
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized = imutils.resize(
    image,
    width=int(image.shape[1] * 2),
    height=int(image.shape[0] * 2),
    inter=cv2.INTER_LINEAR,
)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
