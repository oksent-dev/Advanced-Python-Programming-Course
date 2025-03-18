"""
7. Efekty przy skalowaniu w dół
a. Zmniejsz obraz 5x przy użyciu INTER_AREA .
b. Sprawdź, jak zmienia się jakość w porównaniu do innych metod.
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
    width=int(image.shape[1] / 5),
    height=int(image.shape[0] / 5),
    inter=cv2.INTER_AREA,
)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
