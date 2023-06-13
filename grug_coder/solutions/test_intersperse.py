from intersperse import intersperse
import pytest
from typing import List

@pytest.mark.parametrize("numbers, delimiter, expected_output", [([], 4, []),
                                                                 ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
                                                                 ([10, 20, 30, 40], 2, [10, 2, 20, 2, 30, 2, 40])])

def test_intersperse(numbers: List[int], delimiter: int, expected_output: List[int]):
    from .module import intersperse #import the function here
    assert intersperse(numbers, delimiter) == expected_output
