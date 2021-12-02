"""Testing Multiplication"""
from calc.math_operations.multiplication import Multiplication
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/multiplication_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        multiplication = Multiplication(tup)
        assert multiplication.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/multiplication_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        multiplication = Multiplication(tup)
        assert multiplication.get() == result
