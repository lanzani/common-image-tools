import cv2
import numpy as np

from common_image_tools import tool

def main():
    img = cv2.imread("imgs/test.jpg")
    black = cv2.imread("imgs/black.jpg")

    # Create one channel mask with the same size of the image
    mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    # Draw a rectangle on the mask
    cv2.rectangle(mask, (100, 100), (500, 500), (255, 255, 255), -1)

    # img = tool.merge_color(img, mask, (125, 110, 100))
    img = tool.merge_texture(img, mask, black)

    cv2.imshow("img", img)
    cv2.waitKey(0)




if __name__ == "__main__":
    main()