"""
3. Usuwanie szumu za pomocą otwarcia
a. Wczytaj obraz z szumem (np. solnym i pieprzowym) i/lub obrazy typu
Google Captcha.
b. Zastosuj operację otwarcia z różnymi rozmiarami elementu strukturalnego.
c. Porównaj wyniki przed i po operacji, oceniając skuteczność usuwania
szumu.

===========================================================
W wyniku operacji otwarcia szum solny został usunięty, natomiast
szum pieprzowy pozostał. Mały tekst stał sie nieczytelny.
"""

import cv2
import numpy as np


def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy = image.copy()
    total_pixels = image.size

    num_salt = int(total_pixels * salt_prob)
    coords = [np.random.randint(0, i, num_salt) for i in image.shape]
    noisy[coords[0], coords[1]] = 255

    num_pepper = int(total_pixels * pepper_prob)
    coords = [np.random.randint(0, i, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy


print("Loading images...")
image = cv2.imread("polygons.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit(0)

_, image = cv2.threshold(image, 231, 255, cv2.THRESH_BINARY_INV)
image = salt_and_pepper_noise(image, 0.01, 0.01)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
image_opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


cv2.imshow("Noisy Image", image)
cv2.imshow("Opening Result", image_opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
