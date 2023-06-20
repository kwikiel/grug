from typing import List
import pytest

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not isinstance(paren_string, str):
        raise TypeError("Input must be a string")

    result = []
    for group in paren_string.split():
        level, max_level = 0, 0
        for char in group:
            if char == "(":
                level += 1
                max_level = max(max_level, level)
            elif char == ")":
                level -= 1
                if level < 0:
                    raise ValueError("Invalid parentheses nesting")
        
        if level != 0:
            raise ValueError(f"Unbalanced parentheses: {group}")
        result.append(max_level)

    return result

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('() ()() ()') == [1, 1, 1]
    assert parse_nested_parens('((((()))))) ((())) () ((((()))))') == [8, 3, 1, 6]
    assert parse_nested_parens(')()(()') == ValueError
    assert parse_nested_parens('()(()') == ValueError
    assert parse_nested_parens('(()))') == ValueError
    assert parse_nested_parens('((()())') == ValueError
    assert parse_nested_parens(123) == TypeError
