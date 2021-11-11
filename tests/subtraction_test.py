"""Testing Subtraction"""
from calc.math_operations.subtraction import Subtraction


def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    mynumbers = (1.0, 2.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == -3
