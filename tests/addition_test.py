"""Testing Addition"""
from calc.math_operations.addition import Addition
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/addition_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        addition = Addition(tup)
        assert addition.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/addition_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        addition = Addition(tup)
        assert addition.get() == result
