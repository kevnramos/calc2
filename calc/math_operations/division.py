"""Multiplication Class"""
from calc.math_operations.calculation import Calculation


class Division(Calculation):
    """Division calculation object"""

    def get(self):
        """get the Division results"""
        try:
            result = self.values[0]
            fixed_values = self.values[1:]
            for value in fixed_values:
                result = result / value
            return result
        except ZeroDivisionError:
            return ZeroDivisionError