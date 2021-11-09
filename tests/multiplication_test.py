"""Testing Multiplication"""
from calc.math_operations.multiplication import Multiplication


def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    # Arrange
    mynumbers = (11.0, 21.0)
    multiplication = Multiplication(mynumbers)
    # Act
    # Assert
    assert multiplication.get_result() == 231
