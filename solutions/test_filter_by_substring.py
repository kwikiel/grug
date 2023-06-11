from filter_by_substring import filter_by_substring
import pytest

from typing import List


def test_empty_list():
    assert filter_by_substring([], 'a') == []

def test_no_matching_strings():
    assert filter_by_substring(['hi', 'bye', 'python'], 'a') == []

def test_one_matching_string():
    assert filter_by_substring(['apple', 'banana', 'cherry'], 'a') == ['apple']

def test_multiple_matching_strings():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_matching_substring_is_empty_string():
    assert filter_by_substring(['xyz', 'x', 'y', 'z'], '') == ['xyz', 'x', 'y', 'z']

def test_case_sensitive():
    assert filter_by_substring(['Horse', 'Cat', 'dog'], 'h') == []

    with pytest.raises(AssertionError):
       assert filter_by_substring(['Horse', 'Cat', 'dog'], 'h') == ['Horse']
