from unittest import mock

import pytest

from calculator import calculator


class TestClass:
    def test_file_notfound_error(self):
        with mock.patch('builtins.input', return_value = 10), pytest.raises(FileNotFoundError):
            calculator('./unknown.xlsx', 0)

    def test_key_error(self):
        with mock.patch('builtins.input', return_value = 10), pytest.raises(KeyError):
            calculator('./values.xlsx', 7)
    
    def test_zero_division_error(self):
        with mock.patch('builtins.input', return_value = 0), pytest.raises(ZeroDivisionError):
            calculator('./values.xlsx', 0)