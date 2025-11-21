"""Armstrong number detection module.

This module provides functionality to determine if a number is an Armstrong number.
An Armstrong number (also known as a narcissistic number) is a number that is equal
to the sum of its own digits each raised to the power of the number of digits.

For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
"""


def is_armstrong_number(number: int) -> bool:
    """Check if a number is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number
    that is equal to the sum of its own digits each raised to the power of
    the number of digits.

    Args:
        number: The integer to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.

    Examples:
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(10)
        False
    """
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))
