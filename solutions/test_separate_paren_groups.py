from separate_paren_groups import separate_paren_groups
def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_no_paren_group():
    assert separate_paren_groups("no groups here") == []

def test_separate_paren_groups_single_balanced_group():
    assert separate_paren_groups("( )") == ["()"]

def test_separate_paren_groups_multiple_balanced_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

def test_separate_paren_groups_single_unbalanced_group():
    assert separate_paren_groups("( ) ( ( )") == []

def test_separate_paren_groups_mixed_groups():
    assert separate_paren_groups("( ) (( )) ( ( )") == ["()", "(())"]

def test_separate_paren_groups_space_within_group():
    assert separate_paren_groups("( ) ( ( a b c d ) )") == ["()", "((abcd))"]
