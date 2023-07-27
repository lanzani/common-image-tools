# create and save a 4k black image
import cv2
import numpy as np

img = np.zeros((2160, 3840, 3), np.uint8)
cv2.imwrite("../imgs/black.jpg", img)
