# -*- coding: utf-8 -*-
import colorsys

import numpy as np
from PIL import Image

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)


def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = (h + hout) % 1
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr


def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert("RGBA")
    arr = np.array(np.asarray(img).astype("float"))
    new_img = Image.fromarray(shift_hue(arr, hue / 360.0).astype("uint8"), "RGBA")

    return new_img


# load pil image
image = Image.open("../imgs/test_car.jpg")

# colorize the image
colorized_image = colorize(image, 360)

# show the image
colorized_image.show()
