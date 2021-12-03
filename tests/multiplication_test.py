"""Testing Multiplication"""
from datetime import datetime
from calc.math_operations.multiplication import Multiplication
from Reader_CSV.reader import CsvReader
from Writer_CSV.writer import CsvWriter


def testing_csv_small():
    """Testing mult csv"""
    test_file = CsvReader("tests/operation_files_test/multiplication_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        multiplication = Multiplication(tup)
        dataframe = ['0-0', datetime.now(), 'multiplication_small.csv',
                     f'{i[0][0]}*{i[0][1]}={result}',
                     multiplication.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert multiplication.get() == result


def testing_csv_big():
    """Testing mult csv"""
    test_file = CsvReader("tests/operation_files_test/multiplication_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        multiplication = Multiplication(tup)
        dataframe = ['0-0', datetime.now(), 'multiplication_big.csv',
                     f'{i[0][0]}*{i[0][1]}={result}',
                     multiplication.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert multiplication.get() == result
