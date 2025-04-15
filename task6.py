"""
6. Interaktywna analiza parametrów
a. Zbuduj prosty interfejs przy użyciu cv2.createTrackbar , który pozwoli:
i. zmieniać blockSize (wartości nieparzyste: 3-51),
ii. zmieniać C w zakresie -20 do 20.
b. Umożliw interaktywną eksplorację wpływu tych parametrów na wynik
segmentacji.
c. Przetestuj zbudowany algorytm na przykładowym zdjęciu, dla którego
dobierzesz optymalne parametry C oraz blockSize .
"""

import cv2


def update_threshold(*args):
    block_size = cv2.getTrackbarPos("Block Size", "Adaptive Threshold")
    C = cv2.getTrackbarPos("C", "Adaptive Threshold")

    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3

    adaptive_thresh = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C
    )

    cv2.imshow("Adaptive Threshold", adaptive_thresh)


image = cv2.imread("notes.jpg")
if image is None:
    print("Error: Image not found.")
    exit(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Adaptive Threshold", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Block Size", "Adaptive Threshold", 11, 51, update_threshold)
cv2.createTrackbar("C", "Adaptive Threshold", 2, 20, update_threshold)

update_threshold()

cv2.waitKey(0)
cv2.destroyAllWindows()
