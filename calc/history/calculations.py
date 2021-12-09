"""Calculation history Class"""
from calc.math_operations.addition import Addition
from calc.math_operations.subtraction import Subtraction
from calc.math_operations.multiplication import Multiplication
from calc.math_operations.division import Division


class Calculations:
    """Calculations class manages the history of math_operations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of math_operations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_item():
        """get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_item()
        return calculation.get()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def append_to_history(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation_to_history(values):
        """create an addition and add object to history using factory method create"""
        Calculations.append_to_history(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation_to_history(values):
        """create a subtraction object to history using factory method create"""
        Calculations.append_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.append_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.append_to_history(Division.create(values))
        return True
