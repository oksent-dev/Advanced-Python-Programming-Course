"""
3. Eksperymentuj z rozdzielczością obrazu
a. Zmieniaj rozmiar obrazu wejściowego przed detekcją konturów. Sprawdź,
jak zmiana rozdzielczości wpływa na liczbę i jakość wykrytych konturów.
b. Czy zmniejszenie obrazu może poprawić detekcję?
==========
Zmniejszenie obrazu może poprawić detekcję, ponieważ zmniejsza liczbę pikseli,
co może prowadzić do uproszczenia konturów. Z drugiej strony może ją również pogorszyć,
bo prowadzi do utraty szczegółów. Wydaje sie, że rozsądnym podejściem jest zmniejszenie obrazu
w nieagresywny sposób.
"""

import cv2
import matplotlib.pyplot as plt

print("Loading images...")
image = cv2.imread("kostka.png")

if image is None:
    print("Error: Image not found.")
    exit(0)

resolutions = [1.0, 0.5, 0.25]
mode = cv2.RETR_EXTERNAL

plt.figure(figsize=(12, 8))
for i, scale in enumerate(resolutions, start=1):
    resized_image = cv2.resize(
        image, (int(image.shape[1] * scale), int(image.shape[0] * scale))
    )
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 140, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, mode, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = resized_image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (255, 0, 0), 2)
    plt.subplot(1, len(resolutions), i)
    plt.imshow(cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2RGB))
    plt.title(f"Scale: {int(scale * 100)}%")
    plt.axis("off")

plt.tight_layout()
plt.show()
