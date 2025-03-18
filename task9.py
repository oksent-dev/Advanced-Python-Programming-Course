"""
9. Zapis przyciętego obrazu
a. Przytnij obraz do obszaru o wymiarach 300x300 pikseli.
b. Zapisz wynik jako nowy plik cropped_image.jpg .
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

cropped = image[0:300, 0:300]

cv2.imwrite("cropped_image.jpg", cropped)
print("Cropped image saved as cropped_image.jpg.")

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
