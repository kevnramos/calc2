"""Testing the Calculator"""

from calculator.main import Calculator
from calculator.main import inc


def test_calculator_history():
    """testing calculator result is 0"""
    calc = Calculator()
    assert len(calc.history) == 0


def test_calculator_inc():
    """Testing the inc function of the calculator"""
    assert inc(4) == 5


def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 4) == 5


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(21, 11) == 10


def test_calculator_multiply():
    """Testing the multiply method of the calculator"""
    assert Calculator.multiply_number(7, 3) == 21


def test_calculator_divide():
    """Testing the divide method of the calculator"""
    assert Calculator.divide_number(33, 11) == 3


def test_calculator_divide_by_zero():
    """Testing the divide method of the calculator dividing by zero"""
    assert Calculator.divide_number(50, 0) == ZeroDivisionError
