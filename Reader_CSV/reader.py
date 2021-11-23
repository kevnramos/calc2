import pandas as pd
from pathlib import Path


def absolute_path(filepath):
    relative = Path(filepath)
    return relative.absolute()


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        self.reader(absolute_path(filepath))

    def reader(self, filepath):
        df = pd.read_csv(filepath)
        for index, row in df.iterrows():
            self.data.append([row['value1'], row['value2'], row['result']])

# def reader(filepath):
#     df = pd.read_csv(filepath)
#     data = []
#     for index, row in df.iterrows():
#         data.append([row['value1'], row['value2'], row['result']])
#
#     print(data)
#
#
# reader("/Users/kevin/PycharmProjects/calc2/tests/operation_files_test/addition_small.csv")
