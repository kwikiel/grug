from grug_coder.below_zero import below_zero
def test_below_zero():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([100, -50, 25, -75]) == True
    assert below_zero([0]) == False
    assert below_zero([]) == False
    assert below_zero([10, 20, -30, 40, -50]) == True
