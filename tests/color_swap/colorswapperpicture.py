import cv2
import numpy as np

# read image with alpha
img = cv2.imread("../imgs/test_car.jpg", cv2.IMREAD_UNCHANGED)

# extract bgr channels
bgr = img[:,:,0:3]


# convert bgr to gray as value channel
V = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# create saturation channel
S = np.full_like(V, (0))

# create blue hue channel
# blue is hue=240, but in OpenCV divide by 2
H = np.full_like(V, (0))

# merge HSV
hsv = cv2.merge([H,S,V])

# convert hsv to bgr
bgr_colorized = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# put alpha channel back
result = bgr_colorized.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)

# save result
cv2.imwrite('gray_car_colorized.png', result)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()