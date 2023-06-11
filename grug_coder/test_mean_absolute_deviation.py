from grug_coder.mean_absolute_deviation import mean_absolute_deviation
import pytest
from typing import List
from mean_absolute_deviation import mean_absolute_deviation

def test_mean_absolute_deviation():
    assert mean_absolute_deviation([0]) == 0.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([1.0, 4.0, 6.0, 8.0]) == 2.5
    assert mean_absolute_deviation([2.0, 8.0, 11.0, 17.0]) == 4.5
    with pytest.raises(TypeError):
        mean_absolute_deviation(["hello", "world"]) # type error
