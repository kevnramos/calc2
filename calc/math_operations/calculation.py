"""Calculation Class"""
import pprint


class Calculation:
    """ calculation abstract base class"""

    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.tuple_to_list(values)

    @staticmethod
    def tuple_to_list(values):
        """ standardize values to list of floats"""
        return list(values)
