"""Multiplication Class"""
import numpy
from calc.math_operations.calculation import Calculation


class Multiplication(Calculation):
    """Multiplication calculation object"""

    def get(self):
        """get the multiplication results"""
        return numpy.prod(self.values)
