"""
This module provides functions to calculate the number of grains on a chessboard
based on the classic wheat and chessboard problem.
"""


def square(number: int) -> int:
    """
    Returns the number of grains on a given square of a chessboard.

    Args:
        number (int): The square number (1 to 64).
    Returns:
        int: The number of grains on the specified square.
    Raises:
        ValueError: If the square number is not between 1 and 64.
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total() -> int:
    """
    Returns the total number of grains on the chessboard.

    Returns:
        int: The total number of grains on all 64 squares.
    """
    return 2**64 - 1
