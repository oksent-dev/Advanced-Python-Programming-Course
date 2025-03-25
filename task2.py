"""
2. Zastosowanie operacji XOR do wykrywania różnic między obrazami
a. Wczytaj dwa podobne obrazy z drobnymi różnicami.
b. Użyj cv2.bitwise_xor , aby uwidocznić różnice między nimi.
"""

import cv2

print("Loading images...")
image = cv2.imread("example.jpg")
image2 = cv2.imread("example.jpg")

if image is None:
    print("Error: Image 1 not found.")
    exit(0)

roi = image[0:300, 150:400]
image2[0:300, 400:650] = roi

xor_operator = cv2.bitwise_xor(image, image2)

cv2.imshow("XOR", xor_operator)

cv2.waitKey(0)
cv2.destroyAllWindows()
