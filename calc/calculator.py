""" This is the increment function"""
from calc.math_operations.addition import Addition
from calc.math_operations.subtraction import Subtraction
from calc.math_operations.multiplication import Multiplication
from calc.math_operations.division import Division


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def clear():
        """ Clear the calculation history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def get_all_calculations(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]

    @staticmethod
    def get_last_calculation():
        """ get last calculation from history"""
        return Calculator.history[-1]

    @staticmethod
    def add_nums(*args):
        """ adds list of numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get()

    @staticmethod
    def subtract_nums(*args):
        """ subtract a list of numbers from result"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get()

    @staticmethod
    def multiply_nums(*args):
        """ multiplication number from result"""
        multiplication = Multiplication(args)
        Calculator.history.append(multiplication)
        return multiplication.get()

    @staticmethod
    def divide_nums(*args):
        """ division number from result"""
        division = Division(args)
        Calculator.history.append(division)
        return division.get()
