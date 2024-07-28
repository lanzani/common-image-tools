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
