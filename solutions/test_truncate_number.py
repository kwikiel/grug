from truncate_number import truncate_number
def test_truncate_number():
    # Test a whole number
    assert truncate_number(5) == 0

    # Test a small fractional number
    assert truncate_number(0.25) == 0.25

    # Test a larger fractional number
    assert truncate_number(3.14159) == pytest.approx(0.14159)

    # Test an integer input
    with pytest.raises(TypeError):
        truncate_number(10)

    # Test a negative number
    with pytest.raises(ValueError):
        truncate_number(-2.5)
