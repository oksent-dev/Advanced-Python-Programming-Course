"""
4. Numeryzacja kostek
a. Zmodyfikuj pętlę iterującą po konturach tak, by na każdej kostce (nad jej
środkiem) narysować numer porządkowy ( cv2.putText ).
b. Dodaj zapisywanie każdej wyciętej kostki do osobnego pliku kostka_01.png ,
kostka_02.png , itd.
"""

import cv2
import os


print("Loading images...")
image = cv2.imread("kostka.png")

if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 140, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_area = 500
max_area = 50000
filtered_contours = [
    contour for contour in contours if min_area < cv2.contourArea(contour) < max_area
]
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
image_with_annotations = image.copy()

for i, contour in enumerate(filtered_contours, start=1):
    x, y, w, h = cv2.boundingRect(contour)
    cropped_brick = image[y : y + h, x : x + w]
    filename = os.path.join(output_dir, f"kostka_{i:02d}.png")
    cv2.imwrite(filename, cropped_brick)

    center_x, center_y = x + w // 2, y + h // 2
    cv2.putText(
        image_with_annotations,
        str(i),
        (center_x - 10, center_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
    )


cv2.imshow("Kostki", image_with_annotations)
cv2.waitKey(0)
cv2.destroyAllWindows()
