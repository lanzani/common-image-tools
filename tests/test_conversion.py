import pytest
import dlib
from common_image_tools.conversion import tuple_to_rect, rect_to_tuple


class TestTupleToRect:
    @pytest.mark.parametrize("bbox, expected_rect", [
        ((0, 0, 10, 10), dlib.rectangle(0, 0, 10, 10)),
        ((-5, -5, 10, 10), dlib.rectangle(-5, -5, 5, 5)),
        ((100, 200, 30, 40), dlib.rectangle(100, 200, 130, 240)),
    ])
    def test_valid_bboxes(self, bbox, expected_rect):
        rect = tuple_to_rect(bbox)
        assert rect == expected_rect


class TestRectToTuple:
    @pytest.mark.parametrize("rect, expected_tuple", [
        (dlib.rectangle(0, 0, 10, 10), (0, 0, 10, 10)),  # Test case 1
        (dlib.rectangle(-5, -5, 5, 5), (-5, -5, 10, 10)),  # Test case 2
        (dlib.rectangle(100, 200, 130, 240), (100, 200, 30, 40)),  # Test case 3
        # Add more test cases for other scenarios
    ])
    def test_rect_to_tuple(self, rect, expected_tuple):
        assert rect_to_tuple(rect) == expected_tuple
