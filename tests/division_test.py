"""Testing Division"""
from datetime import datetime
from calc.math_operations.division import Division
from Reader_CSV.reader import CsvReader
from Writer_CSV.writer import CsvWriter


def testing_csv_small():
    """Testing div csv"""
    test_file = CsvReader("tests/operation_files_test/division_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        division = Division(tup)
        dataframe = ['0-0', datetime.now(), 'division_small.csv', f'{i[0][0]}-{i[0][1]}={result}',
                     division.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert division.get() == result


def testing_csv_big():
    """Testing div csv"""
    test_file = CsvReader("tests/operation_files_test/division_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        division = Division(tup)
        dataframe = ['0-0', datetime.now(), 'division_big.csv', f'{i[0][0]}÷{i[0][1]}={result}',
                     division.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        rounder = round(division.get(), 7)
        assert rounder == result


def testing_zero():
    """Testing div csv"""

    test_file = CsvReader("tests/operation_files_test/division_zero.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        division = Division(tup)
        dataframe = ['0-0', datetime.now(), 'division_zero.csv',
                     f'{i[0][0]}÷{i[0][1]}={result}',
                     division.get() == result]
        CsvWriter("./results/exception_log.csv", 'a', dataframe, False)

    assert division.get() == ZeroDivisionError
    assert result == '#DIV/0!'
