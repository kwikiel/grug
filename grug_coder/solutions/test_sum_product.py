from sum_product import sum_product
def test_empty_list():
    assert sum_product([]) == (0, 1)
    
def test_single_item_list():
    assert sum_product([5]) == (5, 5)
    
def test_positive_numbers_list():
    assert sum_product([2, 3, 5, 7]) == (17, 210)
    
def test_negative_numbers_list():
    assert sum_product([-2, 3, -5, 7]) == (3, 210)
    
def test_mixture_of_positives_and_negatives():
    assert sum_product([2, -3, 5, -7]) == (-3, 210)
    
def test_list_with_zero():
    assert sum_product([2, 3, 0, 4]) == (9, 0)
