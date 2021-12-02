"""Testing Subtraction"""
from calc.math_operations.subtraction import Subtraction
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/subtraction_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        subtraction = Subtraction(tup)
        assert subtraction.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/subtraction_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        subtraction = Subtraction(tup)
        assert subtraction.get() == result
