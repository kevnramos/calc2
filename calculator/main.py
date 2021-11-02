""" This is the increment function"""


def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1


class Calculator:
    """ This is the Calculator class"""

    result = 0

    history = []

    # @staticmethod
    # def get_result(self):
    #     """ Get Result of Calculation"""
    #     return self.result

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        result = value_a + value_b

        return result

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        result = value_a - value_b
        return result

    @staticmethod
    def multiply_number(value_a, value_b):
        """ multiply number from result"""
        result = value_a * value_b
        return result

    @staticmethod
    def divide_number(value_a, value_b):
        """ divide number from result"""
        try:
            result = value_a / value_b
            return result
        except ZeroDivisionError:
            return ZeroDivisionError
