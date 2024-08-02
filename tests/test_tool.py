# -*- coding: utf-8 -*-
import numpy as np

import pytest
from PIL.Image import Image

from common_image_tools.tool import (
    create_cv2_image,
    opencv_built_with_gstreamer,
    movement_detection,
    merge_color,
    create_pil_image,
)


def test_create_cv2_image():
    # Test case 1: Check if the returned image has the correct dimensions and color
    size = (100, 200)
    color = (0, 255, 0)
    img = create_cv2_image(size, color)
    assert img.shape == (size[0], size[1], 3)  # Check dimensions
    assert np.all(img == color)  # Check color

    # Test case 2: Check if the returned image is of the correct type
    assert isinstance(img, np.ndarray)

    # Test case 3: Check if the function raises a TypeError when input types are incorrect
    with pytest.raises(TypeError):
        create_cv2_image("invalid_size", color)
    with pytest.raises(ValueError):
        create_cv2_image(size, "invalid_color")


def test_movement_detection():
    # Create two identical images
    img1 = np.zeros((100, 100, 3), dtype=np.uint8)
    img2 = img1.copy()

    # Test no movement
    assert movement_detection(img1, img2) == False

    # Create movement by changing a region in img2
    img2[40:60, 40:60] = 255
    assert movement_detection(img1, img2) == True

    # Test with different thresholds
    assert movement_detection(img1, img2, area_threshold=1000) == False
    assert movement_detection(img1, img2, area_threshold=100) == True


def test_merge_color():
    # TODO improve the test
    # Create a simple image and mask
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    mask = np.zeros((100, 100), dtype=np.uint8)
    mask[25:75, 25:75] = 255

    # Test merging with red color
    red_color = (255, 0, 0)  # RGB
    result = merge_color(image, mask, red_color)

    # Check if the masked area is red in BGR format
    # assert np.all(result[50, 50] == [0, 0, 255])  # BGR
    assert np.all(result[0, 0] == [0, 0, 0])  # Should be black outside the mask


def test_create_pil_image():
    size = (100, 200)
    color = (255, 0, 0)  # Red in RGB
    img = create_pil_image(size, color)

    assert isinstance(img, Image)
    assert img.size == size
    assert img.getpixel((0, 0)) == color


def test_create_cv2_image():
    size = (100, 200)
    color = (0, 0, 255)  # Red in BGR
    img = create_cv2_image(size, color)

    assert isinstance(img, np.ndarray)
    assert img.shape == (100, 200, 3)
    assert np.all(img[0, 0] == color)
