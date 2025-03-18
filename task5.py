"""
5. Zastosowanie odbicia na wybranym obszarze
a. Wczytaj obraz i wytnij z niego fragment (np. środek obrazu lub prawą
połowę).
b. Odbij tylko wycięty fragment i wklej go z powrotem do obrazu.
"""

import cv2
import imutils

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Image not found.")
    exit(0)

height, width = image.shape[:2]

start_x = int(width / 4)
start_y = int(height / 4)
end_x = int(width * 3 / 4)
end_y = int(height * 3 / 4)
cropped = image[start_y:end_y, start_x:end_x]

flipped = cv2.flip(cropped, -1)

image[start_y:end_y, start_x:end_x] = flipped

cv2.imshow("flipped", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
