
from math_series.series import fibonacci, lucas, sum_series


# 0, 1, 1, 2, 3, 5, 8, 13, ...

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fibonacci_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


# 2, 1, 3, 4, 7, 11, 18, 29, ...
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


def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series_zero():
    actual = 0
    expected = sum_series(0)
    assert actual == expected


def test_sum_series_one():
    actual = 1
    expected = sum_series(1)
    assert actual == expected


def test_sum_series_zero_locus(x=2, y=1):
    actual = 2
    expected = sum_series(0, x, y)
    assert actual == expected


def test_sum_series_one_locus(x=2, y=1):
    actual = 1
    expected = sum_series(1, x, y)
    assert actual == expected


def test_sum_series_four_locus(x=2, y=1):
    actual = 7
    expected = sum_series(4, x, y)
    assert actual == expected
