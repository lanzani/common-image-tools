# -*- coding: utf-8 -*-
import numpy as np

import pytest
from common_image_tools.tool import create_cv2_image


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
