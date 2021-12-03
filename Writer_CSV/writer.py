"""write csv files"""
from pathlib import Path
import pandas as pd


def absolute_path(filepath):
    """get absolute path"""
    relative = Path(filepath)
    return relative.absolute()


def writer(filepath, mode, dataframe, header):
    """
    used to write csv files
    """
    if header:
        df = pd.DataFrame([dataframe],  # pylint: disable=invalid-name
                          columns=['Record Number', 'Time', 'Filename', 'Operation',
                                   'Result'])
        df.to_csv(filepath, index=False, mode=mode)
    else:
        df = pd.DataFrame([dataframe])  # pylint: disable=invalid-name
        df.to_csv(filepath, index=False, mode=mode, header=header)


class CsvWriter:  # pylint: disable=too-few-public-methods
    """process csv"""

    def __init__(self, filepath, mode, dataframe, header):
        """constructor"""
        writer(absolute_path(filepath), mode, dataframe, header)
