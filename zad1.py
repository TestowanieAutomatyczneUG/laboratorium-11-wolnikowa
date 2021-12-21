import os
import unittest
from unittest.mock import mock_open, patch, MagicMock
from unittest import mock

class FileOperations:

    def read(self, path):
        result = ""
        with open(path, "r+") as f:
            for line in f:
                result += line
        return result

    def write(self, path, text):
        with open(path, "w+") as f:
            f.write(text)

    def delete(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            raise IOError("file doesn't exist")


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.temp = FileOperations()

    def test_OpenFile_read(self):
        open_test = mock_open(read_data="tutaj jest tekst")
        path = 'zadanko.txt'

        with patch('builtins.open', open_test):
            self.assertEqual("tutaj jest tekst", self.temp.read(path))

    def test_OpenFile_write(self):
        open_test = mock_open(read_data="tutaj jest tekst")
        path = 'zadanko.txt'

        with patch('builtins.open', open_test):
            self.temp.write(path, "To jest inny tekst niz wczesniej")

        open_test.assert_called_once_with(path, 'w+')

    @mock.patch('zad1.os')
    def test_OpenFile_delete_file_exists(self, mock_os):
        path = 'zadanko.txt'
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = True

        self.temp.delete(path)

        mock_os.remove.assert_called_with(path)

    @mock.patch('os.path.exists')
    def test_OpenFile_delete_file_doesnt_exist(self, mock_os):
        path = 'zadanko.txt'
        mock_os.path = MagicMock()
        mock_os.path.exists.return_value = False

        self.assertRaises(IOError, self.temp.delete, path)


if __name__ == '__main__':
    unittest.main()