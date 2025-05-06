"""
6. Filtrowanie konturów po wielkości
a. Zaimplementuj filtrację konturów - usuwaj bardzo małe lub bardzo duże
kontury
b. Zastosowanie: Eliminacja szumu lub niepożądanych obiektów.
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

min_area = 100
max_area = 50000
print(f"Number of contours before filtering: {len(contours)}")
filtered_contours = [
    contour for contour in contours if min_area < cv2.contourArea(contour) < max_area
]
print(f"Number of contours after filtering: {len(filtered_contours)}")

for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Filtered Contours", image)
cv2.waitKey(0)
