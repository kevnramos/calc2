"""Testing the Calculator"""

from calculator.main import Calculator
from calculator.main import inc


def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_inc():
    """Testing the inc function of the calculator"""
    assert inc(4) == 5


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.add_number(1)
    # Assert that the results are correct
    assert calc.result == 1


def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1


def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    calc = Calculator()
    calc.result = 7
    calc.multiply_number(3)
    assert calc.get_result() == 21


def test_calculator_divide():
    """Testing the divide method of the calculator"""
    calc = Calculator()
    calc.result = 33
    calc.divide_number(11)
    assert calc.get_result() == 3


def test_calculator_divide_by_zero():
    """Testing the divide method of the calculator dividing by zero"""
    calc = Calculator()
    calc.result = 50
    assert calc.divide_number(0) == ZeroDivisionError
