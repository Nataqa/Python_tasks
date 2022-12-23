import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()
    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2
    def test_multi_success(self):
        assert self.calc.multiply(2, 3) == 6
    def test_sub_success(self):
        assert self.calc.subtraction(5, 3) == 2
    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
    def test_divizion(self):
        assert self.calc.division(9, 3) == 3
    def teardown(self):
        print("Выполнение метода Teardown")
    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) == 3



