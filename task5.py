"""
5. Zastosowanie arytmetyki do detekcji zmian w obrazach
a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami (np.
obiekt przesunięty).
b. Oblicz ich różnicę ( cv2.absdiff(image1, image2) ).
c. Zinterpretuj wynik - jakie zmiany są widoczne?

Interpretacja:
Różnica pomiędzy dwoma obrazami pozwala na wykrycie zmian w obrazie.
Identyczne obszary na obu obrazach będą czarne, a obszary różniące się będą wyświetlone w kolorze.
"""

import cv2
import numpy as np

print("Loading images...")
image = cv2.imread("example.jpg")
image2 = cv2.imread("example.jpg")

if image is None:
    print("Error: Image 1 not found.")
    exit(0)

roi = image[0:300, 150:400]
image2[0:300, 400:650] = roi

difference = cv2.absdiff(image, image2)

cv2.imshow("Difference", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()
