"""Testing Division"""
from calc.math_operations.division import Division
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/division_small.csv").data
    for i in test_file:
        val1 = i[0]
        val2 = i[1]
        my_tuple = (val1, val2)
        result = i[2]
        division = Division(my_tuple)
        assert division.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/division_big.csv").data
    for i in test_file:
        val1 = i[0]
        val2 = i[1]
        my_tuple = (val1, val2)
        result = i[2]
        division = Division(my_tuple)
        assert division.get() == result

def testing_zero():
    my_tuple = (50, 0)
    division = Division(my_tuple)
    assert division.get() == ZeroDivisionError
