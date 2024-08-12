"""Circle module - get_circle_area, get_circle_circumference
"""
import math


def get_circle_area(radius):
    """calculate area of circle.
    Parameter:
    radius - the radius value to find area
    Result:
    Gives the area of circle value for the given radius"""
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be a numeric value")
    return math.pi * radius ** 2


def get_circle_circumference(radius):
    """calculate circumference of circle.
    Parameter:
    radius - the radius value to find area
    Result:
    Gives the circumference of circle value for the given radius"""
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be a numeric value")
    return 2 * math.pi * radius


def test_get_circle_area():
    """Test case for area of circle"""
    radius = 5
    expected_area = 78.54
    actual_area = get_circle_area(radius)
    assert abs(actual_area - expected_area) < 0.01
    f"Expected {expected_area},but got {actual_area}"
    print(f"Circle area test passed: {actual_area}")


def test_get_circle_circumference():
    """Test case for circumference of circle"""
    radius = 5
    expected_circumfer = 31.42
    actual_circumfer = get_circle_circumference(radius)
    assert abs(actual_circumfer - expected_circumfer) < 0.01
    f"Expected {expected_circumfer}, but got {actual_circumfer}"
    print(f"Circle circumference test passed: {actual_circumfer}")
