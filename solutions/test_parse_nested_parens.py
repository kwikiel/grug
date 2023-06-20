from parse_nested_parens import parse_nested_parens
def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_single_group():
    assert parse_nested_parens('()()()') == [1]

def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    
def test_parse_nested_parens_invalid_input():
    with pytest.raises(TypeError):
        parse_nested_parens(1234)
    with pytest.raises(ValueError):
        parse_nested_parens('((())())')
