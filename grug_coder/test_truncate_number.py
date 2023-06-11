from grug_coder.truncate_number import truncate_number
import pytest

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(0.12345) == 0.12345
    assert truncate_number(10) == 0
    assert truncate_number(-3.5) == None
    assert truncate_number("") == None
