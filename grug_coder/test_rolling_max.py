from grug_coder.rolling_max import rolling_max
import pytest

from typing import List, Tuple


def test_rolling_max_example() -> None:
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_empty_list() -> None:
    assert rolling_max([]) == []


def test_rolling_max_single_element() -> None:
    assert rolling_max([1]) == [1]


def test_rolling_max_all_equal() -> None:
    assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]


def test_rolling_max_reversed_sequence() -> None:
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_rolling_max_negative_elements() -> None:
    assert rolling_max([-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]

