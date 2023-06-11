from grug_coder.parse_nested_parens import parse_nested_parens
def test_parse_nested_parens():
    assert(parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3])
    assert(parse_nested_parens('() () ()') == [1, 1, 1])
    assert(parse_nested_parens('(((())))) (((())))') == [5, 5])
    assert(parse_nested_parens('()') == [1])
    assert(parse_nested_parens('') == [])
