from mean_absolute_deviation import mean_absolute_deviation
def test_mean_absolute_deviation():
    # Test case 1
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    
    # Test case 2
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0
    
    # Test case 3
    assert mean_absolute_deviation([2.0, 4.0, 6.0, 8.0]) == 2.0
    
    # Test case 4
    assert mean_absolute_deviation([]) == 0.0
    
    # Test case 5
    assert mean_absolute_deviation([-1.0, 0.0, 1.0]) == 0.6666666666666666
