import pytest


class Test003:

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.smoke
    def test_sum_007(self):
        a = 10
        b = 2
        print(f"Sum of {a} + {b} = {a + b}")
        assert a + b == 12

    @pytest.mark.math # @pytest.mark.group_name
    @pytest.mark.smoke
    def test_mul_008(self):
        a = 9
        b = 20
        print(f"Mul of {a} * {b} = {a * b}")
        assert a * b == 180

