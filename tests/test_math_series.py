from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0)
    expected = fibonacci(0)
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = lucas(1)
    assert actual == expected