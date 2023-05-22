import unittest
from custom_modules.FileValidator import (
    file_exists as fileexists,
    is_file as isfile,
    is_readable as isreadable,
    is_writable as iswritable,
    is_dir as isdir,
)
from custom_modules.PlatformConstants import (
    LINE_SEP as lsep,
    USER_DIR as udir,
    SEP as sep,
)
from custom_modules.FileOperator import (
    write_file as writefile,
    save_to_file_thread as savenewfile,
    delete_file as deletefile,
    append_to_file_thread as appendtofile,
)

data1 = "The quick brown fox jumped over the lazy dogs."
data2 = "THat quick brown fox successfully jumped the dogs.{}Appended to this file{}".format(
    lsep, lsep
)
dir_name = "fileoperatordir"
file_name = "create_new_file_test.txt"
file_path = "{}{}{}{}{}".format(udir, sep, dir_name, sep, file_name)


def create_new_file():
    global file_path
    global created_new_file
    try:
        savenewfile(file_path, data1)
    except TypeError as te:
        print("{}\n".format(te))


def append_to_file():
    global file_path
    try:
        appendtofile(file_path, data2)
    except TypeError as te:
        print("{}\n".format(te))


class FileOperator(unittest.TestCase):
    def setUp(self):
        global file_path

        create_new_file()
        self.assertTrue(fileexists(file_path) == True)

    def test_append_to_file(self):
        global file_path
        append_to_file()

        with open(file_path, "r") as f:
            for line in f:
                print("{}".format(line))
        self.assertTrue(fileexists(file_path) == True)


if __name__ == "__main__":
    unittest.main()
