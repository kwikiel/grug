from parse_nested_parens import parse_nested_parens
def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_single_group():
    assert parse_nested_parens('()()()()') == [1]
    assert parse_nested_parens('(())()()') == [2]
    assert parse_nested_parens('()()()()()()()()') == [1]
    assert parse_nested_parens('((()))') == [3]

def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens('(()) ((()))') == [2, 3]
    assert parse_nested_parens('(()) () () ((())) ()') == [1, 1, 1, 3]
    assert parse_nested_parens('(()()) () ((())) ((())()())') == [2, 1, 3]
