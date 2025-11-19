"""
Collatz Conjecture Calculator

This module implements the Collatz conjecture (also known as the 3n + 1 problem).
The conjecture states that for any positive integer, repeatedly applying the following
rules will eventually reach 1:
- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add 1
"""


def steps(number: int) -> int:
    """
    Calculate the number of steps required to reach 1 using the Collatz conjecture.

    The Collatz conjecture algorithm applies the following rules repeatedly:
    - If n is even: n = n / 2
    - If n is odd: n = 3n + 1

    Args:
        number (int): A positive integer to start the sequence from.

    Returns:
        int: The number of steps required to reach 1.

    Raises:
        ValueError: If the input number is zero or negative.

    Examples:
        >>> steps(1)
        0
        >>> steps(16)
        4
        >>> steps(12)
        9
        >>> steps(1000000)
        152
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1
    return count
