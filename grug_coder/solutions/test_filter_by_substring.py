from filter_by_substring import filter_by_substring
import pytest

from typing import List

from app import filter_by_substring

def test_filter_by_substring_empty_list():
    result = filter_by_substring([], 'a')
    assert result == []

def test_filter_by_substring_single_match():
    result = filter_by_substring(['abc'], 'a')
    assert result == ['abc']

def test_filter_by_substring_multiple_matches():
    result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    assert result == ['abc', 'bacd', 'array']

def test_filter_by_substring_no_matches():
    result = filter_by_substring(['def', 'efg', 'fgh'], 'a')
    assert result == []

def test_filter_by_substring_substring_empty():
    with pytest.raises(ValueError):
        filter_by_substring(['abc', 'bacd', 'cde', 'array'], '')
