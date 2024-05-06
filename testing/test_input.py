from unittest import mock

from calculator import calculator


class TestClass:
    def test_positive_int(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator('./values.xlsx', 0) == 894

    def test_negative_int(self):
        with mock.patch('builtins.input', return_value = -20):
            assert calculator('./values.xlsx', 0) == 224

    def test_positive_float(self):
        with mock.patch('builtins.input', return_value = 10.33):
            assert calculator('./values.xlsx', 0) == 838

    def test_negative_float(self):
        with mock.patch('builtins.input', return_value = -9.89):
            assert calculator('./values.xlsx', 0) == 914                                    