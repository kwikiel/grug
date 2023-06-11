from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    output_list = []
    for i in range(len(numbers) - 1):
        output_list.append(numbers[i])
        output_list.append(delimiter)
    if numbers:
        output_list.append(numbers[-1])
    return output_list