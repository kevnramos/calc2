"""Testing Division"""
from calc.math_operations.division import Division


def test_calculation_division():
    """testing that our calculator has a static method for division"""
    mynumbers = (100.0, 2.0)
    division = Division(mynumbers)
    assert division.get_result() == 50
