import pytest


def my_func(x, y, z):
    return x + y + z

def my_exception():
    div = 10/ 0
    return div

class TestClass:
    def test_result1(self):
        assert my_func(1, 2, 3) == 5, 'The result should be 6'
    
    def test_result2(self):
        assert my_func(1, 2, 3) == 6

def test_result3():
    with pytest.raises(ZeroDivisionError):
        my_exception()
