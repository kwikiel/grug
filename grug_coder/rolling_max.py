from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []
    current_max = None
    for i, num in enumerate(numbers):
        if i == 0:
            current_max = num
            max_numbers.append(current_max)
        else:
            current_max = max(current_max, num)
            max_numbers.append(current_max)
    return max_numbers