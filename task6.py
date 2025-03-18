"""
6. Kopiowanie i wklejanie fragmentu obrazu
a. Przytnij określony fragment obrazu (np. o wymiarach 100x100 pikseli).
b. Wklej ten fragment w inne miejsce na obrazie.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

roi = image[0:300, 150:400]
image[0:300, 400:650] = roi

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
