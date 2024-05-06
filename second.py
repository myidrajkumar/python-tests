import pytest


def my_exception():
    div = 10 / 0
    return div

def test_result1():
    with pytest.raises(ZeroDivisionError):
        my_exception()