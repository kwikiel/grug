import math
import pytest


def truncate_number(number: float) -> float:
    """Given a floating point number or integer, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1). Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, (float, int)):
        raise TypeError(f"Expected float or int, got {type(number).__name__}")
    _, decimal_part = math.modf(number)
    return decimal_part


def test_truncate_number():
    # Test a whole number
    assert truncate_number(5) == 0.0

    # Test a small fractional number
    assert truncate_number(0.25) == 0.25

    # Test a larger fractional number
    assert truncate_number(3.14159) == pytest.approx(0.14159)

    # Test a negative number
    assert truncate_number(-3.5) == 0.5

    # Test an integer input
    assert truncate_number(4) == 0.0

    # Test a zero input
    assert truncate_number(0) == 0.0
    
    # Test edge case of large floating point number
    assert truncate_number(1.234e100) == pytest.approx(7.856481330802942e-01)
