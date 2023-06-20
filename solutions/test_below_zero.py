from below_zero import below_zero
def test_below_zero_empty_list():
    assert not below_zero([])


def test_below_zero_single_operation():
    assert not below_zero([10])
    assert below_zero([-10])


def test_below_zero_multiple_operations():
    assert not below_zero([10, 20, 30])
    assert not below_zero([10, -10, 20])
    assert below_zero([10, -10, -5])
    assert below_zero([10, -5, -10, 20])
    assert below_zero([10, 20, -35, 5, 10])

    
def test_below_zero_large_numbers():
    assert not below_zero([1000000000, 2000000000])
    assert not below_zero([1000000000, -2000000000, 1500000000, -500000000])
    assert below_zero([100000000000, -50000000000, 200000000000, -250000000000])
    
    
def test_below_zero_decimal_numbers():
    assert not below_zero([0.5, 1.5])
    assert below_zero([0.5, 1.5, -2.5, 3.5])
    assert below_zero([0.5, -0.5, 0.1, -0.1])
    

def test_below_zero_mixed_types():
    assert not below_zero([10, 20, 30, -40, -50, 60])
    assert not below_zero([10, 20, 30, -40.5, -50, 60])
    assert below_zero([10, 20, 30, -40.5, -50, 60, "70"])
