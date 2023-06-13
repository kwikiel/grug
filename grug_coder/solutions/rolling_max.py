from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = []
    current_max = float('-inf')
    for num in numbers:
        current_max = max(num, current_max)
        max_so_far.append(current_max)
    return max_so_far
