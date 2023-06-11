from grug_coder.sum_product import sum_product
def test_empty_list():
  assert sum_product([]) == (0, 1)

def test_positive_numbers():
  assert sum_product([1, 2, 3, 4]) == (10, 24)

def test_single_number():
  assert sum_product([5]) == (5, 5)

def test_negative_numbers():
  assert sum_product([-1, -2, -3, -4]) == (-10, -24)

def test_mix_of_positive_and_negative_numbers():
  assert sum_product([1, -2, 3, -4]) == (-2, 24)

def test_zero_only():
  assert sum_product([0]) == (0, 0)

def test_mix_of_zero():
  assert sum_product([0, 1, 0]) == (1, 0)

def test_large_numbers():
  assert sum_product([1000, 500, 200]) == (1700, 100000000)

def test_large_numbers_negative_and_positive():
  assert sum_product([-1000, 500, -100]) == (-600, 50000000)

