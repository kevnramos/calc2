""" This is the increment function"""
from calc.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_last_calculation():
        """ This is the gets the result of the calculation"""
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def clear():
        """THis gets first index of history"""
        return Calculations.clear_history()

    @staticmethod
    def get_first_calculation():
        """THis gets first index of history"""
        return Calculations.get_first_calculation()

    @staticmethod
    def get_specified_calculation(num):
        """This gets specific index of history list"""
        return Calculations.get_calculation(num)

    @staticmethod
    def addition(tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition_calculation_to_history(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation_to_history(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation_to_history(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """ division number from result"""
        Calculations.add_division_calculation_to_history(tuple_values)
        return True

    @staticmethod
    def getHistoryFromCSV():
        """ Get history """
        return Calculations.readHistoryFromCSV()

    @staticmethod
    def writeHistoryToCSV(data):
        """ Get history """
        return Calculations.writeHistoryToCSV(data)
