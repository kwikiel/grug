from mean_absolute_deviation import mean_absolute_deviation
def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0
    assert mean_absolute_deviation([-1.0, 1.0, -1.0, 1.0]) == 1.0
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) == 1.2
    assert mean_absolute_deviation([1.0]) == 0.0
    assert mean_absolute_deviation([-1.0, -2.0, 0.0, 2.0]) == 1.25
