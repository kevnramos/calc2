# pylint: disable-all
"""Testing the Calculator"""
import pytest
from calc.history.calculations import Calculations
from calc.math_operations.addition import Addition
from calc.math_operations.subtraction import Subtraction
from calc.math_operations.multiplication import Multiplication
from calc.math_operations.division import Division


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    Calculations.clear_history()


@pytest.fixture
def multiple_values_fixture():
    """default addition"""
    tup = (100, 10)
    division = Division(tup)
    Calculations.append_to_history(division)
    tup = (11, 7)
    addition = Addition(tup)
    Calculations.append_to_history(addition)
    subtraction = Subtraction(tup)
    Calculations.append_to_history(subtraction)
    multiplication = Multiplication(tup)
    Calculations.append_to_history(multiplication)


@pytest.fixture
def addition_fixture():
    """default addition"""
    tup = (11, 7)
    addition = Addition(tup)
    Calculations.append_to_history(addition)


@pytest.fixture
def subtraction_fixture():
    """default subtraction"""
    tup = (11, 7)
    subtraction = Subtraction(tup)
    Calculations.append_to_history(subtraction)


@pytest.fixture
def division_fixture():
    """default division"""
    tup = (100, 10)
    division = Division(tup)
    Calculations.append_to_history(division)


@pytest.fixture
def multiplication_fixture():
    """default multiplication"""
    tup = (11, 7)
    multiplication = Multiplication(tup)
    Calculations.append_to_history(multiplication)


def test_addition_history(clear_history_fixture, addition_fixture):
    assert Calculations.count_history() == 1


def test_addition_values(clear_history_fixture, addition_fixture):
    assert Calculations.get_calculation(0).get() == 18
    assert Calculations.get_first_calculation().get() == 18


def test_subtraction_history(clear_history_fixture, subtraction_fixture):
    assert Calculations.count_history() == 1


def test_subtraction_values(clear_history_fixture, subtraction_fixture):
    assert Calculations.get_calculation(0).get() == 4
    assert Calculations.get_first_calculation().get() == 4


def test_division_history(clear_history_fixture, division_fixture):
    assert Calculations.count_history() == 1


def test_division_values(clear_history_fixture, division_fixture):
    assert Calculations.get_calculation(0).get() == 10
    assert Calculations.get_first_calculation().get() == 10


def test_multiplication_history(clear_history_fixture, multiplication_fixture):
    assert Calculations.count_history() == 1


def test_multiplication_values(clear_history_fixture, multiplication_fixture):
    assert Calculations.get_calculation(0).get() == 77
    assert Calculations.get_first_calculation().get() == 77


def test_history(clear_history_fixture, multiple_values_fixture):
    assert Calculations.get_first_calculation().get() == 10
    assert Calculations.get_last_calculation_result_value() == 77
    assert Calculations.get_calculation(1).get() == 18
    assert Calculations.get_calculation(2).get() == 4
