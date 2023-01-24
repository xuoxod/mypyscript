import os
from .Utils import numbered_date_time_stamp as timestamp, make_directory
from .FileOperator import append_data_to_file as append_to_file
from .PlatformConstants import USER_DIR as udir, SEP as sep, LINE_SEP as lsep


def log_this(operation, dir_name="log_directory"):
    script_log_dir_pathname = "{}{}{}".format(udir, sep, dir_name)
    if not os.path.exists(script_log_dir_pathname):
        dir_created = make_directory(script_log_dir_pathname)

        if dir_created:
            stamp = "{}| {}{}".format(timestamp(), operation, lsep)
            file_path = "{}{}app.log".format(script_log_dir_pathname, sep)
            return append_to_file(file_path, stamp)
        else:
            print("Directory not created")
    else:
        stamp = "{}| {}{}".format(timestamp(), operation, lsep)
        file_path = "{}{}app.log".format(script_log_dir_pathname, sep)
        return append_to_file(file_path, stamp)


def create_log(operation, dir_name="log_directory", log_name="app.log"):
    script_log_dir_pathname = "{}{}{}".format(udir, sep, dir_name)
    if not os.path.exists(script_log_dir_pathname):
        dir_created = make_directory(script_log_dir_pathname)

        if dir_created:
            stamp = "{}| {}{}".format(timestamp(), operation, lsep)
            file_path = "{}{}{}".format(script_log_dir_pathname, sep, log_name)
            return append_to_file(file_path, stamp)
        else:
            print("Directory not created")
    else:
        stamp = "{}| {}{}".format(timestamp(), operation, lsep)
        file_path = "{}{}{}".format(script_log_dir_pathname, sep, log_name)
        return append_to_file(file_path, stamp)
