# -*- coding: utf-8 -*-
from typing import Tuple

import numpy as np

from unittest.mock import patch
import pytest

from common_image_tools.operation import (
    bbox_centroid,
    is_point_in_bbox,
    is_point_in_shape,
    scale_bboxes,
    resize_image_with_aspect_ratio,
)


class TestBboxCentroid:
    @pytest.mark.parametrize(
        "bbox, expected_centroid",
        [
            ((0, 0, 10, 10), (5, 5)),
            ((-5, -5, 10, 10), (0, 0)),
            ((100, 200, 30, 40), (115, 220)),
        ],
    )
    def test_bbox_centroid(self, bbox, expected_centroid):
        centroid = bbox_centroid(bbox)
        assert centroid == expected_centroid

    @pytest.mark.parametrize(
        "bbox",
        [
            (-10, -10, 20, 20),
            (0, 0, 15, 15),
            (1000, 2000, 300, 400),
        ],
    )
    def test_valid_bboxes(self, bbox: Tuple[int, int, int, int]):
        centroid = bbox_centroid(bbox)
        assert isinstance(centroid, Tuple)
        assert len(centroid) == 2
        assert all(isinstance(coord, int) for coord in centroid)


# Test resize_image_with_aspect_ratio function
def test_resize_image_with_aspect_ratio():
    # Create a mock image
    mock_image = np.zeros((100, 200, 3), dtype=np.uint8)

    # Define the target size
    target_size = (50, 50)

    # Calculate the expected new dimensions
    aspect_ratio = 200 / 100  # width / height of the original image
    if aspect_ratio > 1:
        expected_width = 50
        expected_height = int(50 / aspect_ratio)
    else:
        expected_height = 50
        expected_width = int(50 * aspect_ratio)

    # Create the expected resized image
    expected_resized = np.zeros((expected_height, expected_width, 3), dtype=np.uint8)

    with patch("cv2.resize", return_value=expected_resized) as mock_resize:
        result = resize_image_with_aspect_ratio(mock_image, target_size)

    assert result.shape == (expected_height, expected_width, 3)
    mock_resize.assert_called_once_with(mock_image, (expected_width, expected_height))


# Test is_point_in_bbox function
@pytest.mark.parametrize(
    "point, bbox, expected",
    [
        ((5, 5), (0, 0, 10, 10), True),
        ((15, 15), (0, 0, 10, 10), False),
        ((0, 0), (0, 0, 10, 10), False),
        ((10, 10), (0, 0, 10, 10), False),
    ],
)
def test_is_point_in_bbox(point, bbox, expected):
    assert is_point_in_bbox(point, bbox) == expected


# Test is_point_in_shape function
def test_is_point_in_shape():
    shape_contour = [(0, 0), (10, 0), (10, 10), (0, 10)]

    with patch("cv2.pointPolygonTest", return_value=1) as mock_pointPolygonTest:
        result = is_point_in_shape((5, 5), shape_contour)

    assert result == True
    mock_pointPolygonTest.assert_called_once()


# Test scale_bboxes function
def test_scale_bboxes():
    bboxes = [(10, 10, 20, 20), (30, 30, 40, 40)]
    scale_factor = 2

    result = scale_bboxes(bboxes, scale_factor)

    assert result == [(20, 20, 40, 40), (60, 60, 80, 80)]


# Test bbox_centroid function
@pytest.mark.parametrize(
    "bbox, expected",
    [
        ((0, 0, 10, 10), (5, 5)),
        ((10, 10, 20, 20), (20, 20)),
        ((5, 5, 15, 25), (12, 17)),
    ],
)
def test_bbox_centroid(bbox, expected):
    assert bbox_centroid(bbox) == expected
