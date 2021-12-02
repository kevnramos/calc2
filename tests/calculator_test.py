"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return Calculator.clear()


# @pytest.fixture
# def default_test():
#     return Calculator.add_nums(34, 75)
#     return Calculator.subtract_nums(34, 75)
#     return Calculator.multiply_nums(34, 75)
#     return Calculator.divide_nums(10, 100)
#     return Calculator.divide_nums(10, 0)


# def test_history(clear_history_fixture, default_test):
#     assert Calculator.get_first_calculation() == default_test
#     assert Calculator.get_last_calculation() == ZeroDivisionError
#     assert Calculator.get_specified_calculation(0) == 109
#     assert Calculator.get_specified_calculation(1) == -41
#     assert Calculator.get_specified_calculation(2) == 2550
#     assert Calculator.get_specified_calculation(3) == .1
#     assert Calculator.get_specified_calculation(4) == ZeroDivisionError
#     assert Calculator.splice_history(0, 3) == [109, -41, 2550, .1]
#     assert Calculator.get_size_of_history() == 5
#
#     Calculator.clear()
#     assert Calculator.get_size_of_history() == 0
#     assert Calculator.clear() == True

# You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    assert Calculator.add(1.0, 11.0) == 12.0


def test_calculator_add_static_multiple(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    assert Calculator.add(1.0, 3.0, 44.0) == 48.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtract(1.0, 2.0) == -1.0


def test_calculator_subtract_static_multiple(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtract(10.0, 2.0, 3.0) == 5.0


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    assert Calculator.multiply(1.0, 2.0) == 2.0


def test_calculator_multiply_static_multiple(clear_history_fixture):
    """Testing the multiply method of the calc"""
    assert Calculator.multiply(11.0, 2.0, 5.0) == 110.0


def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    assert Calculator.divide(125.0, 25.0) == 5.0


def test_calculator_divide_static_mulitple(clear_history_fixture):
    """Testing the divide method of the calc"""
    assert Calculator.divide(725.0, 5.0, 20) == 7.25


def test_calculator_history_static_property(clear_history_fixture):
    """Testing the length method of the calc"""
    Calculator.add(1.0, 2.0)
    assert len(Calculator.history) == 1


def test_clear_history():
    """Testing clear history returns true for success"""
    Calculator.add(1.0, 2.0)
    assert Calculator.clear() == True


def test_get_calculation(clear_history_fixture):
    Calculator.add(1.0, 2.0)
    assert Calculator.get_specified_calculation(0).get() == 3


def test_get_calculation_last(clear_history_fixture):
    Calculator.add(1.0, 2.0)
    assert Calculator.get_last_calculation().get() == 3


def test_get_calculation_first(clear_history_fixture):
    Calculator.add(1.0, 22.0)
    Calculator.add(1.0, 2.0)
    assert Calculator.get_first_calculation().get() == 23
    assert Calculator.get_size_of_history() == 2
