from rolling_max import rolling_max
import pytest
from typing import List, Tuple

def test_rolling_max_empty():
    assert rolling_max([]) == []

def test_rolling_max_single_element():
    assert rolling_max([10]) == [10]

def test_rolling_max_all_same():
    assert rolling_max([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_rolling_max_example():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    
def test_rolling_max_negative_numbers():
    assert rolling_max([10, -2, 0, 5, -8]) == [10, 10, 10, 10, 5]

def test_rolling_max_with_duplicates():
    assert rolling_max([1, 2, 2, 2, 3, 2, 4]) == [1, 2, 2, 2, 3, 3, 4]
    
def test_rolling_max_large_list():
    lst = list(range(10**4))
    assert rolling_max(lst) == lst
    
