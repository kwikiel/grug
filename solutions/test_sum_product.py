from sum_product import sum_product
import pytest
from typing import List, Tuple

from {filename} import sum_product

def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)

def test_sum_product_single_element_list():
    assert sum_product([4]) == (4, 4)

def test_sum_product_positive_elements():
    assert sum_product([3,7,5,9]) == (24, 945)

def test_sum_product_mixed_elements():
    assert sum_product([-5, 4, -7]) == (-8, 140)

def test_sum_product_zero():
    assert sum_product([3, 0, 9]) == (12, 0)
