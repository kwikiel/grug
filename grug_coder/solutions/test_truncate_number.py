from truncate_number import truncate_number
import pytest
from math import isclose
from your_module import truncate_number

def test_truncate_number():
    assert isclose(truncate_number(3.5), 0.5)
    assert isclose(truncate_number(4.0), 0.0)
    assert isclose(truncate_number(2.25), 0.25)
    assert isclose(truncate_number(1.987654321), 0.987654321)

def test_truncate_number_raises_exception():
    with pytest.raises(TypeError):
        truncate_number('3.5')
    with pytest.raises(ValueError):
        truncate_number(-3.5)
