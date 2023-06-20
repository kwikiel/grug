from has_close_elements import has_close_elements
import pytest

def test_has_close_elements_returns_false_for_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_returns_false_for_list_with_single_item():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_returns_false_for_list_with_distinct_numbers():
    assert has_close_elements([1.0, 2.0, 3.0], 1.0) == False

def test_has_close_elements_returns_true_for_list_with_close_numbers():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_has_close_elements_returns_true_for_list_with_negative_numbers():
    assert has_close_elements([-1.0, -2.0, 0.5, 2.0, 3.0], 0.8) == True
