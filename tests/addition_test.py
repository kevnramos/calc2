"""Testing Addition"""
from datetime import datetime
from calc.math_operations.addition import Addition
from Reader_CSV.reader import CsvReader
from Writer_CSV.writer import CsvWriter


def testing_csv_small():
    """Testing add csv"""
    test_file = CsvReader("tests/operation_files_test/addition_small.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        addition = Addition(tup)
        dataframe = ['0-0', datetime.now(), 'addition_small.csv',
                     f'{i[0][0]}+{i[0][1]}={result}',
                     addition.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert addition.get() == result


def testing_csv_big():
    """Testing add csv"""
    test_file = CsvReader("tests/operation_files_test/addition_big.csv").data
    for i in test_file:
        tup = (i[0])
        result = i[1]
        addition = Addition(tup)
        dataframe = ['0-0', datetime.now(), 'addition_big.csv',
                     f'{i[0][0]}+{i[0][1]}={result}',
                     addition.get() == result]
        CsvWriter("./results/test_log.csv", 'a', dataframe, False)
        assert addition.get() == result
