"""Testing Division"""
from calc.math_operations.division import Division
from Reader_CSV.reader import CsvReader


def testing_csv_small():
    test_file = CsvReader("tests/operation_files_test/division_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        division = Division(tup)
        assert division.get() == result


def testing_csv_big():
    test_file = CsvReader("tests/operation_files_test/division_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        division = Division(tup)
        assert division.get() == result

def testing_zero():
    tup = (50, 0)
    division = Division(tup)
    assert division.get() == ZeroDivisionError
