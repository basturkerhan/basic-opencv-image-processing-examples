import cv2 # import Opencv
import numpy as np # import Numpy

img = cv2.imread('histo-photo.jpeg', 0) # read a image using imread
equ = cv2.equalizeHist(img) # creating a Histograms Equalization of a image using cv2.equalizeHist()
res = np.hstack((img, equ)) # stacking images side-by-side
cv2.imshow('photo: ', res)  # show image input vs output

cv2.waitKey(0)