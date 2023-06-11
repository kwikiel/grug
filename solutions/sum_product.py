from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # empty list
        return 0, 1

    product = 1
    for n in numbers:
        product *= n

    return sum(numbers), product
