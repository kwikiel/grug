from grug_coder.intersperse import intersperse

def test_intersperse_empty_list():
    assert intersperse([], 4) == []

def test_intersperse():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

def test_intersperse_one_element_list():
    assert intersperse([9], 1) == [9]

def test_intersperse_repeating_delimeter():
    assert intersperse([6, 3, 1], 3) == [6, 3, 3, 1]

def test_intersperse_large_input():
    assert intersperse([i for i in range(1, 1001)], 0) == [i for i in range(1, 1000)] + [0, 1000]