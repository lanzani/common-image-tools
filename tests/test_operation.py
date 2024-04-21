# -*- coding: utf-8 -*-
import pytest

from common_image_tools.operation import bbox_centroid


class TestBboxCentroid:
    @pytest.mark.parametrize("bbox, expected_centroid", [
        ((0, 0, 10, 10), (5, 5)),
        ((-5, -5, 10, 10), (0, 0)),
        ((100, 200, 30, 40), (115, 220)),
    ])
    def test_bbox_centroid(self, bbox, expected_centroid):
        centroid = bbox_centroid(bbox)
        assert centroid == expected_centroid

    @pytest.mark.parametrize("bbox", [
        (-10, -10, 20, 20),
        (0, 0, 15, 15),
        (1000, 2000, 300, 400),
    ])
    def test_valid_bboxes(self, bbox: tuple[int, int, int, int]):
        centroid = bbox_centroid(bbox)
        assert isinstance(centroid, tuple)
        assert len(centroid) == 2
        assert all(isinstance(coord, int) for coord in centroid)

    # @pytest.mark.parametrize("bbox", [
    #     (0, 0, 10.5, 10.5),
    #     (0, 0, 10, 10, 5),
    # ])
    # def test_invalid_bboxes(self, bbox):
    #     with pytest.raises((TypeError, ValueError)):
    #         bbox_centroid(bbox)
