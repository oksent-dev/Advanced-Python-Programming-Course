"""
8. Animacja przesuwającego się ROI
a. Wczytaj obraz i dynamicznie przesuwaj ROI w poziomie (np. przesunięcie
co 10 pikseli), aby stworzyć efekt „przesuwania kamery”.
b. Wyświetlaj na ekranie kolejne wycinki ROI po kliknięciu w klawiature.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

height, width = image.shape[:2]

roi_width = 300
roi_height = 300
roi_x = 0

while True:
    roi = image[0:roi_height, roi_x : roi_x + roi_width]
    cv2.imshow("ROI", roi)

    key = cv2.waitKey(0)
    if key == 27:
        break

    roi_x += 10
    if roi_x + roi_width > width:
        roi_x = 0

cv2.destroyAllWindows()
