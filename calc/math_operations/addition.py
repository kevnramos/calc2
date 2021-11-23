"""Addition Class"""
from calc.math_operations.calculation import Calculation


class Addition(Calculation):
    """ calculation addition class"""

    def get(self):
        """get the addition results"""
        return sum(self.values)
