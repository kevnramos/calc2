"""Testing Subtraction"""
from datetime import datetime
from calc.math_operations.subtraction import Subtraction
from Reader_CSV.reader import CsvReader
from Writer_CSV.writer import CsvWriter


def testing_csv_small():
    """Testing sub csv"""
    test_file = CsvReader("tests/operation_files_test/subtraction_small.csv").data

    for i in test_file:
        tup = (i[0])
        result = i[1]
        subtraction = Subtraction(tup)

        dataframe = ['0-0', datetime.now(), 'subtraction_small.csv',
                     f'{i[0][0]}-{i[0][1]}={result}',
                     subtraction.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)

        assert subtraction.get() == result


def testing_csv_big():
    """Testing sub csv"""
    test_file = CsvReader("tests/operation_files_test/subtraction_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        subtraction = Subtraction(tup)
        dataframe = ['0-0', datetime.now(), 'subtraction_big.csv',
                     f'{i[0][0]}-{i[0][1]}={result}',
                     subtraction.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert subtraction.get() == result
