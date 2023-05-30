import pytest

import os, sys
sys.path.append(os.path.abspath('../../'))
from task_1_read_file import read_magic_number


def create_file_data(test_data):
    with open('testfile.txt', 'a') as f_o:
        f_o.writelines(test_data)


TEST_DATA_NORMAL = [
                (['0\n', '2\n', '3\n', 'abobus\n'],    False),
                (['1\n', '2\n', '3\n'],                True),
                (['2\n', 'bruh\n', '5\n'],             True),
                (['3\n', '5\n'],                       False),
                (['10\n', 'False\n', 'some string\n'], False) ]                 

@pytest.mark.parametrize('file_data, expected_result', TEST_DATA_NORMAL)
def test_read_magic_number(file_data, expected_result):
    print(file_data)
    create_file_data(file_data)
    assert read_magic_number('testfile.txt') == expected_result






TEST_DATA_ERR_VALUE = [
                        ('string\n', '2\n', '3\n'),
                        ('name\n', 'second name\n'),
                        ('one\n', 'two\n', 'three\n'),
                        ('definetly not int\n', '123\n', '321\n')  ]

@pytest.mark.parametrize('file_data', TEST_DATA_ERR_VALUE)
def test_value_err(file_data):
    print(file_data)
    create_file_data(file_data)
    with pytest.raises(ValueError):
        read_magic_number('testfile.txt')


@pytest.mark.parametrize('filepath', [('123123.txt'), ('cogito_ergo_sum.txt'), ('teeeeeeeeeeeestfile.txt')])
def test_file_not_found(filepath):
    with pytest.raises(FileNotFoundError):
        read_magic_number(filepath)