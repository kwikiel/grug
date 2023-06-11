from intersperse import intersperse
def test_intersperse_empty_list():
    assert intersperse([], 4) == []

def test_intersperse_single_element_list():
    assert intersperse([5], 9) == [5]

def test_intersperse_even_list_length():
    assert intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]

def test_intersperse_odd_list_length():
    assert intersperse([6, 7, 8, 9, 10], 2) == [6, 2, 7, 2, 8, 2, 9, 2, 10]

def test_intersperse_negative_delimiter():
    assert intersperse([11, 12, 13], -2) == [11, -2, 12, -2, 13]
