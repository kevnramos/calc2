"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """Division calculation object"""

    def get_result(self):
        """get the Division results"""
        result = self.values[0]
        fixed_values = self.values[1:]
        for value in fixed_values:
            result = result / value
        return result
