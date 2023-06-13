from mean_absolute_deviation import mean_absolute_deviation
import pytest

from typing import List
from your_module import mean_absolute_deviation

def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected_result = 1.0
    result = mean_absolute_deviation(numbers)
    assert result == expected_result

def test_mean_absolute_deviation_empty_list():
    numbers = []
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation(numbers)

def test_mean_absolute_deviation_one_element():
    numbers = [1.0]
    expected_result = 0.0
    result = mean_absolute_deviation(numbers)
    assert result == expected_result

def test_mean_absolute_deviation_multiple_elements():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_result = 1.2
    result = mean_absolute_deviation(numbers)
    assert result == expected_result

def test_mean_absolute_deviation_float_numbers():
    numbers = [1.3, 2.4, 3.1, 4.5]
    expected_result = 1.075
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(expected_result, 0.01)
