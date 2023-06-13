from has_close_elements import has_close_elements
import pytest



def test_has_close_elements_returns_true_when_close_numbers_exist():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0], 0.5) == True
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([10.4, 20.6, 5.7, 15.1], 0.5) == True

def test_has_close_elements_returns_false_when_no_close_numbers_exist():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0], 0.3) == False
    assert has_close_elements([10.4, 20.6, 5.7, 15.1, 30.8], 4.0) == False

def test_has_close_elements_raises_type_error_if_given_incorrect_arguments():
    with pytest.raises(TypeError):
        has_close_elements("this is not a list", 0.5)

    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], "not a float")

    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, "not a number"], 0.5)
