"""
5. Pomiar wymiarów kostek
a. Dla każdej wykrytej kostki:
i. Oblicz jej szerokość i wysokość w pikselach.
ii. Na oryginalnym obrazie narysuj prostokąt oraz opisz go wymiarami,
np. „40x40 px”.
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

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        image, f"{w}x{h}px", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1
    )

cv2.imshow("kostki", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
