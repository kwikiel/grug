from intersperse import intersperse
def test_intersperse_empty_list():
    assert intersperse([], 4) == []
    
def test_intersperse_one_element_list():
    assert intersperse([5], 2) == [5]
    
def test_intersperse_two_element_list():
    assert intersperse([3, 7], 8) == [3, 8, 7]
    
def test_intersperse_multiple_elements():
    assert intersperse([2, 9, 4, 6], 0) == [2, 0, 9, 0, 4, 0, 6]
    
def test_intersperse_multiple_delimiters():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
