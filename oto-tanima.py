import cv2
import numpy as np

def mask_of_image(image):
    height = image.shape[0]
    polygons = np.array([[(0,height),(2200,height),(250,100)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

img = cv2.imread("photo.jpeg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

maskedImage = mask_of_image(gray_image)

(thresh, output2) = cv2.threshold(maskedImage, 200, 255, cv2.THRESH_BINARY)
output2 = cv2.GaussianBlur(output2, (5, 5), 3)

output2 = cv2.Canny(output2, 180, 255)
cv2.imshow("Canny Image: ", output2)


lines = cv2.HoughLinesP(output2, 1, np.pi/180,30)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),4)
    
cv2.imshow("Image: ", img)
cv2.waitKey(0)