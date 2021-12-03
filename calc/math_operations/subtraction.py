"""Subtraction Class"""
from calc.math_operations.calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get(self):
        """get the subtraction results"""
        result = self.values[0]
        fixed_values = self.values[1:]
        for value in fixed_values:
            result = result - value
        return result
