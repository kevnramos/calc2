"""this will run all tests, write logs, move files, and reset files"""
import os
import time
from Writer_CSV.writer import CsvWriter


def run():
    """This will run tests and make log files"""
    print("Writing headers...")
    dataframe = ['', '', '', '', '']
    CsvWriter("./results/test_log.csv", 'w', dataframe, True)

    print('Testing subtraction...')
    os.system("pytest ./tests/subtraction_test.py ")
    print('Moving subtraction csv files into done_scan folder...')
    os.system('mv tests/operation_files_test/subtraction_* tests/done_scan/')

    print('Testing addition...')
    os.system("pytest ./tests/addition_test.py ")
    os.system('mv tests/operation_files_test/addition_* tests/done_scan/')

    print('Testing division...')
    os.system("pytest ./tests/division_test.py ")
    os.system('mv tests/operation_files_test/division_* tests/done_scan/')

    print('Testing multiplication...')
    os.system("pytest ./tests/multiplication_test.py ")
    os.system('mv tests/operation_files_test/multiplication_* tests/done_scan/')

    print("Finished Scanning input folder.\nScanned CSV files are now in 'tests/done_scan' folder")
    print('All tests are logged')
    print('Success')


def reset():
    """this will reset the file structure and move csv files back to where they were"""
    os.system('mv tests/done_scan/* tests/operation_files_test/')


run()
print('\n\n\n\n================================')
print('Will now reset file structure')
reset()
time.sleep(10)
print('File Structure now reset. You can now rerun the tests')
