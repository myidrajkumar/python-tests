import math
from unittest import mock
import pandas
import pytest


@pytest.fixture
def xyfunc():
    df = pandas.read_excel('./values.xlsx')

    x = float(df['Price'][0])

    with mock.patch('builtins.input', return_value = 10):
        y = float(input('Enter the value of y: '))
    
    return math.pow(x/y, 2)

def test_result(xyfunc):
    result = round(xyfunc)
    assert result == 894