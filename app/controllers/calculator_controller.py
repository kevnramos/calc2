"""controller app"""
from flask import render_template, request, flash, redirect, url_for  # pylint: disable=import-error, unused-import
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator


class CalculatorController(ControllerBase):
    """controller"""

    @staticmethod
    def post():
        """post functions"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2.'
        else:
            flash('Successful Calculation!')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_calculation())

            # data = {
            #     'value1': [value1],
            #     'value2': [value2],
            #     'operation': [operation],
            # }

            data = [str(value1), str(value2), str(operation), result]

            Calculator.writeHistoryToCSV(data)

            return render_template('result.html', value1=value1, data=Calculator.getHistoryFromCSV(), value2=value2,
                                   operation=operation,
                                   result=result)  # pylint: disable=line-too-long
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        """Calculator page"""
        return render_template('calculator2.html')

    @staticmethod
    def triple_a():
        """tripleA page"""
        return render_template('tripleA.html')

    @staticmethod
    def pylint():
        """pylint page"""
        return render_template('pylint.html')

    @staticmethod
    def design():
        """Design page"""
        return render_template('design.html')

    @staticmethod
    def oop():
        """Object oriented page"""
        return render_template('oop.html')

    @staticmethod
    def azure():
        """Azure page"""
        return render_template('azure.html')

    @staticmethod
    def command():
        """CLI page"""
        return render_template('command.html')

    @staticmethod
    def git():
        """Git page"""
        return render_template('git.html')

    @staticmethod
    def docker():
        """Azure page"""
        return render_template('docker.html')
