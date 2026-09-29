import pytest


class Test002:

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.sanity
    def test_sum_005(self):
        a = 10
        b = 2
        print(f"Sum of {a} + {b} = {a + b}")
        assert a + b == 12

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.regression
    def test_mul_006(self):
        a = 9
        b = 20
        print(f"Mul of {a} * {b} = {a * b}")
        assert a * b == 180

