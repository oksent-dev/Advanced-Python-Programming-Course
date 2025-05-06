"""
2. Eksperymentuj z metodą cv2.findContours
a. Na progowanym obrazie znajdź kontury przy użyciu funkcji cv2.findContours .
Narysuj wszystkie wykryte kontury na oryginalnym obrazie w kolorze
czerwonym o grubości 2px.
b. Zmieniaj tryby (parametr mode w funkcji findContours ), przetestuj
cv2.RETR_EXTERNAL , cv2.RETR_TREE i cv2.RETR_LIST i opisz różnice w komentarzu.
==========
cv2.RETR_EXTERNAL - zwraca tylko kontury zewnętrzne, czyli kontury największych obiektów w obrazie.
cv2.RETR_LIST - zwraca wszystkie kontury.
cv2.RETR_TREE - zwraca wszystkie kontury i tworzy hierarchię konturów.
"""

import cv2
import matplotlib.pyplot as plt

print("Loading images...")
image = cv2.imread("kostka.png")

if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 140, 255, cv2.THRESH_BINARY)

modes = [cv2.RETR_EXTERNAL, cv2.RETR_TREE, cv2.RETR_LIST]
mode_names = ["RETR_EXTERNAL", "RETR_TREE", "RETR_LIST"]

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

for i, (mode, mode_name) in enumerate(zip(modes, mode_names), start=2):
    contours, _ = cv2.findContours(binary_image, mode, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (255, 0, 0), 2)
    plt.subplot(2, 2, i)
    plt.imshow(cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2RGB))
    plt.title(f"Contours ({mode_name})")
    plt.axis("off")

plt.tight_layout()
plt.show()
