"""Calculation Class"""
import pprint


class Calculation:
    """ calculation abstract base class"""

    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        return list(values)
