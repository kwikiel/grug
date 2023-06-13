from rolling_max import rolling_max
def test_rolling_max():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert rolling_max([1, 2, 3]) == [1, 2, 3]
    assert rolling_max([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert rolling_max([1]) == [1]
    assert rolling_max([]) == []
