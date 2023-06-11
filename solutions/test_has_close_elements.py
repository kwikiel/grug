from has_close_elements import has_close_elements
import pytest
from typing import List


@pytest.mark.parametrize("numbers, threshold, expected_output", [
    ([], 0.5, False),
    ([1.0], 0.5, False),
    ([1.0, 2.0], 0.5, False),
    ([1.0, 2.9, 3.0], 0.2, True),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 2.0, 3.0], 0.5, False),
    ([2.0, 2.5, 2.8, 3.0, 3.5], 0.4, True),
])
def test_has_close_elements(numbers: List[float], threshold: float, expected_output: bool):
    assert has_close_elements(numbers, threshold) == expected_output

