import os
from .FileValidator import file_exists, is_file, is_readable, is_writable, is_dir
from .TypeTester import arg_is_a_list as aial
from .PlatformConstants import LINE_SEP as lsep


def delete_file(file_path):
    if file_exists(file_path) and is_file(file_path):
        os.remove(file_path)
        return not file_exists(file_path)


def append_data_list_to_file(file_path, list_data):
    if aial(list_data):
        exists = file_exists(file_path)
        isfile = is_file(file_path)
        writable = is_writable(file_path)

        if exists and isfile and writable:
            with open(file_path, "a", 2) as f:
                for d in list_data:
                    f.write(d)

            return file_exists(file_path)
        else:
            with open(file_path, "a", 2) as f:
                for d in list_data:
                    f.write(d)

            return file_exists(file_path)
    return None


def append_data_to_file(file_path, data):
    exists = file_exists(file_path)
    isfile = is_file(file_path)
    writable = is_writable(file_path)

    if exists and isfile and writable:
        with open(file_path, "a", 2) as f:
            f.write(data)
        return file_exists(file_path)
    else:
        with open(file_path, "a", 2) as f:
            f.write(data)
        return file_exists(file_path)


def save_new_file(file_path, data=None):
    if not data == None:
        exists = file_exists(file_path)
        isfile = is_file(file_path)

        if exists and isfile:
            deleted = delete_file(file_path)
            if deleted:
                with open(file_path, "w") as f:
                    f.write(data)
                    f.write(lsep)
                return file_exists(file_path)
        else:
            with open(file_path, "w") as f:
                f.write(data)
                f.write(lsep)
            return file_exists(file_path)
    return None


def write_to_file(file_path, data=None):
    if not data == None:
        string_data = str(data)
        if file_exists(file_path):
            deleted = delete_file(file_path)
            if deleted:
                with open(file_path, "w") as f:
                    f.write(string_data)
        else:
            with open(file_path, "w") as f:
                f.write(string_data)
        return file_exists(file_path)
    return False
