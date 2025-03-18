"""
4. Dynamiczny wybór ROI
a. Napisz skrypt, który pozwala użytkownikowi podać wartości startX , endX ,
startY , endY z klawiatury.
b. Przytnij obraz zgodnie z wprowadzonymi wartościami i wyświetl wynik.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

startX = int(input("Enter startX: "))
endX = int(input("Enter endX: "))
startY = int(input("Enter startY: "))
endY = int(input("Enter endY: "))

roi = image[startY:endY, startX:endX]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
