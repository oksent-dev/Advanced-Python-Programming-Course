"""
5. Automatyczna maska ROI
a. Na obrazie, na którym znajdują się obiekty (np. elementy produkcyjne),
spróbuj wygenerować maskę pierwszego planu.x
b. Z pomocą progowania adaptacyjnego wydziel obiekty i zastosuj
cv2.bitwise_and , aby wyświetlić tylko te regiony z oryginalnego obrazu.
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pyramid.png")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

binary_adaptive = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 5
)
binary_adaptive = cv2.bitwise_not(binary_adaptive)

masked_image = cv2.bitwise_and(image, image, mask=binary_adaptive)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary_adaptive, cmap="gray")
plt.title("Adaptive Threshold Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB))
plt.title("Masked Image")
plt.axis("off")

plt.tight_layout()
plt.show()
