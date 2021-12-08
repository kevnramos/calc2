# pylint: disable-all
"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return Calculator.clear()


def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    assert Calculator.addition(1.0, 11.0) == 12.0


def test_calculator_add_static_multiple(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    assert Calculator.addition(1.0, 3.0, 44.0) == 48.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtraction(1.0, 2.0) == -1.0


def test_calculator_subtract_static_multiple(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtraction(10.0, 2.0, 3.0) == 5.0


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    assert Calculator.multiplication(1.0, 2.0) == 2.0


def test_calculator_multiply_static_multiple(clear_history_fixture):
    """Testing the multiply method of the calc"""
    assert Calculator.multiplication(11.0, 2.0, 5.0) == 110.0


def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    assert Calculator.divide(125.0, 25.0) == 5.0


def test_calculator_divide_static_mulitple(clear_history_fixture):
    """Testing the divide method of the calc"""
    assert Calculator.divide(725.0, 5.0, 20) == 7.25


def test_calculator_history_static_property(clear_history_fixture):
    """Testing the length method of the calc"""
    Calculator.addition(1.0, 2.0)
    assert len(Calculator.history) == 1


def test_clear_history():
    """Testing clear history returns true for success"""
    Calculator.addition(1.0, 2.0)
    assert Calculator.clear() == True


def test_get_calculation(clear_history_fixture):
    Calculator.addition(1.0, 2.0)
    assert Calculator.get_specified_calculation(0).get() == 3


def test_get_calculation_last(clear_history_fixture):
    Calculator.addition(1.0, 2.0)
    assert Calculator.get_last_calculation().get() == 3


def test_get_calculation_first(clear_history_fixture):
    Calculator.addition(1.0, 22.0)
    Calculator.addition(1.0, 2.0)
    assert Calculator.get_first_calculation().get() == 23
    assert Calculator.get_size_of_history() == 2
