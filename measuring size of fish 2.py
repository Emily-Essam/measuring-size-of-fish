import cv2
import imutils
import numpy as np
from matplotlib import pyplot
# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("fish.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#get contour
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image, [cnt], -1, (0, 255, 0), 4)
x, y, w, h = cv2.boundingRect(thresh)
cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
cv2.putText(image, "w={},h={}".format(w, h), (120, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)

cv2.imshow("original",image)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()



