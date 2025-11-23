"""
Triangle module

Contains functions to check if a triangle is equilateral, isosceles, or scalene.
All functions will return False if the input is not a valid triangle.
"""

from functools import wraps


def is_valid_triangle(func):
    """
    Decorator to check if the input is a valid triangle.
    """

    @wraps(func)
    def wrapper(sides):
        a, b, c = sides
        if len(sides) != 3:
            return False
        if any(x <= 0 for x in (a, b, c)):
            return False
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        return func(sides)

    return wrapper


@is_valid_triangle
def equilateral(sides: list) -> bool:
    """
    Check if the triangle is equilateral.

    Parameters:
        sides (list): List of three side lengths.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.
    """
    return sides[0] == sides[1] == sides[2]


@is_valid_triangle
def isosceles(sides: list) -> bool:
    """
    Check if the triangle is isosceles.

    Parameters:
        sides (list): List of three side lengths.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


@is_valid_triangle
def scalene(sides: list) -> bool:
    """
    Check if the triangle is scalene.

    Parameters:
        sides (list): List of three side lengths.

    Returns:
        bool: True if the triangle is scalene, False otherwise.
    """
    return sides[0] != sides[1] != sides[2] != sides[0]
