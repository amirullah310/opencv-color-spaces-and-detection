import cv2
import numpy as np
# from google.colab.patches import cv2_imshow


image = cv2.imread('gedungpnl.jpeg')

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(image_hsv, lower_red, upper_red)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()