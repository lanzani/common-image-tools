# -*- coding: utf-8 -*-
import pytest
from common_image_tools.verification import is_inside


class TestIsInside:
    @pytest.mark.parametrize(
        "point, shape, expected",
        [
            ((50, 50), [(0, 0), (100, 0), (100, 100), (0, 100)], True),  # Point inside the shape
            ((0, 0), [(0, 0), (100, 0), (100, 100), (0, 100)], True),  # Point on the boundary of the shape
            ((150, 150), [(0, 0), (100, 0), (100, 100), (0, 100)], False),  # Point outside the shape
            # ((50, 50), [(0, 0), (100, 0), (100, 100), (0, 100), (20, 20), (80, 20), (80, 80), (20, 80)], True),  # Complex shape with hole, point inside
            ((80, 20), [(0, 0), (100, 0), (100, 100), (0, 100), (20, 20), (80, 20), (80, 80), (20, 80)], True),
            # Complex shape with hole, point on the boundary
            ((150, 150), [(0, 0), (100, 0), (100, 100), (0, 100), (20, 20), (80, 20), (80, 80), (20, 80)], False),
            # Complex shape with hole, point outside
        ],
    )
    def test_is_inside(self, point, shape, expected):
        assert is_inside(point, shape) == expected

    # Add more test methods as needed


# def test_is_inside():
#     # Test with a square
#     square = [(0, 0), (100, 0), (100, 100), (0, 100)]
#
#     assert is_inside((50, 50), square) == True  # Inside
#     assert is_inside((0, 0), square) == True  # On vertex
#     assert is_inside((50, 0), square) == True  # On edge
#     assert is_inside((150, 150), square) == False  # Outside
#
#     # Test with a triangle
#     triangle = [(0, 0), (100, 0), (50, 100)]
#
#     assert is_inside((25, 25), triangle) == True  # Inside
#     assert is_inside((50, 0), triangle) == True  # On edge
#     assert is_inside((0, 0), triangle) == True  # On vertex
#     assert is_inside((75, 75), triangle) == False  # Outside
#
#     # Test with a more complex polygon
#     polygon = [(0, 0), (100, 0), (100, 50), (50, 50), (50, 100), (0, 100)]
#
#     assert is_inside((25, 25), polygon) == True  # Inside
#     assert is_inside((75, 25), polygon) == True  # Inside
#     assert is_inside((25, 75), polygon) == True  # Inside
#     assert is_inside((75, 75), polygon) == False  # Outside
#     assert is_inside((50, 50), polygon) == True  # On internal vertex
#
#     # Test with a concave shape
#     concave = [(0, 0), (100, 0), (100, 100), (75, 50), (50, 100), (25, 50), (0, 100)]
#
#     assert is_inside((50, 25), concave) == True  # Inside
#     assert is_inside((50, 75), concave) == False  # In the "dip" of the concave shape <- ?
#     assert is_inside((12, 75), concave) == True  # Inside one of the "prongs"
#     assert is_inside((88, 75), concave) == True  # Inside the other "prong"
