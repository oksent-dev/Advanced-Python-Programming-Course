"""
3. Przyciemnianie obrazu
a. Zmniejsz jasność obrazu o 80 jednostek.
b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

M = np.ones(image.shape, dtype="uint8") * 80
subtracted = image - M

opencv_subtracted = cv2.subtract(image, M)

cv2.imshow("Subtracted", subtracted)
cv2.imshow("OpenCV Subtracted", opencv_subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
