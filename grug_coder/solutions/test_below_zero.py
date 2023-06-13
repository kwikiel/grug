from below_zero import below_zero
import pytest
from typing import List

from your_module import below_zero


def test_below_zero_empty_list():
    assert below_zero([]) == False

def test_below_zero_single_operation_less_than_zero():
    assert below_zero([-3]) == True

def test_below_zero_single_operation_more_than_zero():
    assert below_zero([7]) == False

def test_below_zero_multiple_operations_with_positive_balance():
    assert below_zero([2, 5, 3]) == False

def test_below_zero_multiple_operations_with_negative_balance():
    assert below_zero([3, -4, 5, -2]) == True

def test_below_zero_multiple_operations_with_zero_balance():
    assert below_zero([1, -1, 3, -3, 2, -2]) == False
