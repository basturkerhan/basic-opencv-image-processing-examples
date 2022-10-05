import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("coin.png")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(thresh, output2) = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)

output2 = cv2.GaussianBlur(output2, (5, 5), 1)

output2 = cv2.Canny(output2, 180, 255)

plt.imshow(output2, cmap = plt.get_cmap("gray"))

circles = cv2.HoughCircles(output2,cv2.HOUGH_GRADIENT,1,10,param1=180,param2=27,minRadius=20,maxRadius=60)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

plt.imshow(img)
plt.show()