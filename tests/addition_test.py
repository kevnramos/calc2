"""Testing Addition"""
from calc.math_operations.addition import Addition
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/addition_small.csv").data
    for i in test_file:
        val1 = i[0]
        val2 = i[1]
        my_tuple = (val1, val2)
        result = i[2]
        addition = Addition(my_tuple)
        assert addition.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/addition_big.csv").data
    for i in test_file:
        val1 = i[0]
        val2 = i[1]
        my_tuple = (val1, val2)
        result = i[2]
        addition = Addition(my_tuple)
        assert addition.get() == result
