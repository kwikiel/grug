from parse_nested_parens import parse_nested_parens
import pytest
from typing import List

# Import the function implementation here
# from parse_nested_parens_file import parse_nested_parens


@pytest.mark.parametrize(
    "paren_string, expected_result",
    [
        ("(()()) ((())) () ((())()())", [2, 3, 1, 3]),
        ("((()))", [3]),
        ("()", [1]),
        ("((()()))", [4]),
        ("()", [1]),
        ("()()()()", [1,1,1,1]),
    ]
)
def test_parse_nested_parens(paren_string: str, expected_result: List[int]):
    assert parse_nested_parens(paren_string) == expected_result
