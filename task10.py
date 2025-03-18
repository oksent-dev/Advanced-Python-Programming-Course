"""
10. Zmiana rozmiaru i zapis pliku
a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku
resized_output.jpg .
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

resized = imutils.resize(image, width=800)

cv2.imwrite("resized_output.jpg", resized)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
