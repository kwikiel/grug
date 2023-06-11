from truncate_number import truncate_number
import pytest
from <module_name> import truncate_number

def test_truncate_number_positive_value():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(6.8) == 0.8
    assert truncate_number(1.2) == 0.2

def test_truncate_number_zero_value():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_negative_value():
    with pytest.raises(ValueError):
        assert truncate_number(-3.5)

def test_truncate_number_string_value():
    with pytest.raises(TypeError):
        assert truncate_number("3.5")
