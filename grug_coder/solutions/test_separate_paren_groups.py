from separate_paren_groups import separate_paren_groups
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('()()()()') == ['()', '()', '()', '()']
    assert separate_paren_groups('(())()') == ['(())', '()']
    assert separate_paren_groups('()(()())()') == ['()', '(()())', '()']
    assert separate_paren_groups('(()) ( ) (( )) (( )( ))') == ['(())', '()', '(())', '(()())']
    assert separate_paren_groups('') == []
