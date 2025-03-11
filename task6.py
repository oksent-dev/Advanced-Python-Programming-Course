"""
6. Zamazywanie szczegółów na zdjęciu
a. Znajdź w Internecie profilowe zdjęcie osoby.
b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
d. Niebieskim okręgiem obejmij dookoła twarz osoby.
"""

import cv2

print("Loading image...")
image = cv2.imread("profile_picture.png")

if image is None:
    print("Error: Can't load image.")
    exit(0)


cv2.circle(image, (370, 470), 60, (0, 0, 255), -1)
cv2.circle(image, (640, 470), 60, (0, 0, 255), -1)
cv2.rectangle(image, (370, 700), (640, 800), (0, 255, 0), -1)
cv2.circle(image, (image.shape[1] // 2, image.shape[0] // 2), 400, (255, 0, 0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
