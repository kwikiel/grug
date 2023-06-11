from separate_paren_groups import separate_paren_groups
def test_separate_paren_groups():
    # Test Case 1
    result = separate_paren_groups('( ) (( )) (( )( ))')
    assert result == ['()', '(())', '(()())']

    # Test Case 2
    result = separate_paren_groups('(( )) ( ) ()')
    assert result == ['(())', '()', '()']

    # Test Case 3
    result = separate_paren_groups('((())()()) (()))()')
    assert result == ['((())()())', '())))']

    # Test Case 4
    result = separate_paren_groups('()()')
    assert result == ['()', '()']

    # Test Case 5
    result = separate_paren_groups('')
    assert result == []
