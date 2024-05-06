
import math
from unittest import mock
import pandas
import pytest


@pytest.fixture(scope='module', params=[0, 1, 2, 3, 4])
def xyfunc(request):
    df = pandas.read_excel('./values.xlsx')

    x = float(df['Price'][request.param])

    with mock.patch('builtins.input', return_value = 10):
        y = float(input('Enter the value of y: '))
    
    return math.pow(x/y, 2)