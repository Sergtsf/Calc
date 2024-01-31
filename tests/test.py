import pytest

from app.tcalculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


### проверить возможность, что сумма двух чисел дает правильный результат ###
    def test_adding_success(self):
        assert self.calc.adding(self, 5, 6) == 11


### проверить возможность, что разность двух чисел дает правильный результат ###
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 12, 2) == 10

### проверить возможность, что произведение двух чисел дает правильный результат ###
    def test_multiply_success(self):
        assert self.calc.multiply(self, 7, 2) == 14

### проверить возможность, что частное двух чисел (целое число) дает правильный результат ###
    def test_division_success(self):
        assert self.calc.division(self, 15, 5) == 3

### проверить возможность, что ввод нулевых значений не вызывает ошибок ###
    def test_zero_success(self):
        assert self.calc.adding(self, 0, 0) == 0


### проверить возможность, что калькулятор правильно обрабатывает отрицательные числа ###
    def test_negative_numbers(self):
        assert self.calc.multiply(self, -3, 3) == -9


### проверить возможность, что калькулятор корректно обрабатывает ввод дробей.
    def test_fractional_numbers(self):
        assert self.calc.adding(self, 1.5, 1.3) == 2.8


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')