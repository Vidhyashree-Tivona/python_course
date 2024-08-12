"""Rectangle module - get_rect_area, get_rect_perimeter"""


def get_rect_area(length, breadth):
    """Calculate area of rectangle
    Parameter:
    Length - the length of rectangle
    breadth - the breadth of rectangle
    Result:
    Gives the value for area of rectangle"""
    if not isinstance(length, (int, float)) or not isinstance(breadth,
                                                              (int, float)):
        raise TypeError("length and breadth must be numeric values")
    return length * breadth


def get_rect_perimeter(length, breadth):
    """Calculate perimeter of rectangle
    Parameter:
    Length - the length of rectangle
    breadth - the breadth of rectangle
    Result:
    Gives the value for perimeter of rectangle"""
    if not isinstance(length, (int, float)) or not isinstance(breadth,
                                                              (int, float)):
        raise TypeError("length and breadth must be numeric values")
    return 2 * (length + breadth)


def test_get_rect_area():
    """Test case for area of rectangle"""
    length = 10
    breadth = 5
    expected_area = 50
    actual_area = get_rect_area(length, breadth)
    assert actual_area == expected_area
    print(f"Rectangle area test passed: {actual_area}")


def test_get_rect_perimeter():
    """Test case for perimeter of rectangle"""
    length = 10
    breadth = 5
    expected_perimeter = 30
    actual_perimeter = get_rect_perimeter(length, breadth)
    assert actual_perimeter == expected_perimeter
    f"Expected {expected_perimeter}, but got {actual_perimeter}"
    print(f"Rectangle perimeter test passed: {actual_perimeter}")
