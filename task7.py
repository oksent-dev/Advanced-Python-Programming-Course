"""
7. Liczenie i raportowanie kostek
a. Na końcu całego procesu wyświetl w terminalu:
i. liczbę wykrytych kostek
ii. ich średnią szerokość i wysokość
iii. minimalny i maksymalny rozmiar
"""

import cv2

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

widths = []
heights = []
size = []

for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    widths.append(w)
    heights.append(h)
    size.append(cv2.contourArea(contour))

if widths and heights:
    avg_width = sum(widths) / len(widths)
    avg_height = sum(heights) / len(heights)
    min_size = min(size)
    max_size = max(size)

    print(f"Number of detected bricks: {len(filtered_contours)}")
    print(f"Average width: {avg_width:.2f} px")
    print(f"Average height: {avg_height:.2f} px")
    print(f"Minimum size: {min_size} px")
    print(f"Maximum size: {max_size} px")
else:
    print("No bricks detected.")
