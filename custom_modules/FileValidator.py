import os
from os import access, R_OK, W_OK, F_OK, X_OK


def file_exists(filePath):
    return os.path.exists(filePath)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)


def is_sym_link(path):
    return os.path.islink(path)


def is_readable(path):
    return access(path, R_OK)


def is_writable(path):
    return access(path, W_OK)
