"""process csv files"""
from pathlib import Path
import pandas as pd


def absolute_path(filepath):
    """get absolute path"""
    relative = Path(filepath)
    return relative.absolute()


class CsvReader: # pylint: disable=too-few-public-methods
    """process csv"""
    data = []

    def __init__(self, filepath):
        """constructor"""
        self.data = []
        self.reader(absolute_path(filepath))

    def reader(self, filepath):
        """
        info being appended -> [(tuple), result]
        first element is a tuple because that is what *args wants
        i do this here instead of appending [1,2,3], and then having to make a tuple in the tests
        """
        df = pd.read_csv(filepath)  # pylint: disable=invalid-name
        for index, row in df.iterrows():  # pylint: disable=unused-variable
            self.data.append([(row['value1'], row['value2']), row['result']])
