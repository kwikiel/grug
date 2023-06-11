from below_zero import below_zero
def test_below_zero():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([]) == False
    assert below_zero([0]) == False
    assert below_zero([-1, 1, 0]) == True
    assert below_zero([-5, -5, 10]) == True
