from grug_coder.filter_by_substring import filter_by_substring
def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []


def test_filter_by_substring_no_match():
    assert filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'x') == []


def test_filter_by_substring_one_match():
    assert filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']


def test_filter_by_substring_all_match():
    assert filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
