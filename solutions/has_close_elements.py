from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, any two numbers are closer to each other than
    the given threshold.

    Args:
        numbers: A list of floats as input.
        threshold: A float value setting the limit for how close two numbers can be without returning True.

    Returns:
        A boolean value representing whether there are any elements in the input list that are closer than the threshold.

    Raises:
        ValueError: If the threshold value is negative, as it is not allowed to be.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
        >>> has_close_elements([-1.0, -2.0, 0.5, 2.0, 3.0], 0.8)
        True
        >>> has_close_elements([], 0.5)
        False
        >>> has_close_elements([1.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.0], 0.5)
        True
        >>> has_close_elements([1.0, 2.0, 0.5, 2.0, 3.0], -0.1)
        Traceback (most recent call last):
            ...
        ValueError: Threshold value cannot be negative
    """
    if threshold < 0:
        raise ValueError("Threshold value cannot be negative")

    if len(numbers) < 2:
        return False

    # sort the input list
    numbers.sort()

    for i in range(len(numbers) - 1):
        # if difference between any two consecutive elements is smaller than or equal to given threshold, return True
        if abs(numbers[i] - numbers[i+1]) <= threshold:
            return True

    return False
