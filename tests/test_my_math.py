import pytest

from my_math import multiply

from my_math.ext import add, subtract


class TestMyMath:
    def test_python_ops(self):
        assert multiply(1, 2) == 2

    def test_cxx_ops(self):
        assert subtract(1, 2) == -1
        assert add(1, 2) == 3
