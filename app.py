#! /usr/bin/python3

import argparse, os
from custom_modules.FileValidator import file_exists, is_file, is_dir, is_readable
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.Utils import exit_prog
from custom_modules.FileDialog import open_file_type
from custom_classes.FileInterrorgator import file_interrogator as file_i
from custom_modules.FileOperator import write_to_file as write_file
from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.MyLogger import create_log as log

cus = cms["custom"]
desc = "This program creates a specfile and runs pyinstaller separately"
epil = "Creates a specification file for use with pyinstaller"
vers = "%prog 0.1"
speci_file_data = "pyi-makespec "
app_log_dir_name = "scriptpackager"
app_error_log_name = "scriptpackager-errors.log"
app_log_name = "scriptpackager-logs.log"
file_type = (
    "python files",
    "*.py",
)


def error_handler(*args):
    e_msg_head = cus(255, 121, 121, "Error ")
    e_msg_body = ""
    for i, a in enumerate(args):
        if i < (len(args) - 1):
            e_msg_body += cus(255, 255, 255, "{}{}".format(a, lsep))
        else:
            e_msg_body += cus(255, 255, 255, "{}".format(a))
    e_msg = "{}\t{}".format(e_msg_head, e_msg_body)
    print("{}{}".format(e_msg, lsep))
    exit_prog()


parser = argparse.ArgumentParser(description=desc, epilog=epil)
parser.error = error_handler
parser.version = vers
get_file = parser.add_mutually_exclusive_group()
specification = parser.add_argument_group()
pyinstaller = parser.add_argument_group()

specification.add_argument_group("script", "Create a specification file")
specification.add_argument(
    "-n",
    "--name",
    dest="name",
    metavar="name",
    nargs=1,
    help="Name the specification file",
)
specification.add_argument(
    "-i", "--icon", dest="icon", metavar="icon", nargs=1, help="Icon file path"
)
specification.add_argument(
    "-s",
    "--splash",
    dest="splash",
    metavar="splash",
    nargs=1,
    help="Splash image file path",
)
specification.add_argument(
    "-l",
    "--log",
    dest="log",
    type=int,
    # choices=["info", "warning", "error", "critical", "trace", "debug"],
    choices=range(1, 7),
    help="Minimum log level. 1=info, 2=warning, 3=error, 4=critical, 5=trace, 6=debug",
)
specification.add_argument(
    "-f",
    "--file",
    dest="file",
    action="store_true",
    help="Single file executable. Default",
)
specification.add_argument(
    "-D", "--dir", dest="dir", action="store_true", help="Directory output"
)
specification.add_argument(
    "-S",
    "--specpath",
    dest="specpath",
    metavar="specpath",
    nargs=1,
    help="Path to save the spec-file. Defaults to current directory.",
)

get_file.add_argument_group("file path", "Handles accessing file path")
get_file.add_argument(
    "-p",
    "--path",
    dest="path",
    metavar="path",
    nargs=1,
    help="Indicates the file path from standard input.",
)
get_file.add_argument(
    "-d",
    "--dialog",
    dest="dialog",
    action="store_true",
    help="Indicates the file path from file dialog.",
)

pyinstaller.add_argument_group("installer", "Packages python script")
pyinstaller.add_argument("-e", "--exe", dest="exe", nargs=1, help="Run pyinstaller")


args = parser.parse_args()

if args.exe:
    file_path = args.exe[0]
    if file_exists(file_path):
        if is_file(file_path):
            if is_readable(file_path):
                file_i.set_path(file_path)
                file_ext = file_i.extension()

                if file_ext == ".py":
                    print("Packaging {} script\n".format(file_path))
                elif file_ext == ".spec":
                    print("Using spec file {}\n".format(file_path))
    exit_prog()

if args.name:
    speci_file_data += "-n {} ".format(args.name[0])

if args.icon:
    icon = args.icon[0]
    if file_exists(icon):
        if is_file(icon):
            if is_readable(icon):
                speci_file_data += "-i {} ".format(icon)

if args.splash:
    splash_file = args.splash[0]
    if file_exists(splash_file):
        if is_file(splash_file):
            if is_readable(splash_file):
                speci_file_data += "--splash {} ".format(splash_file)

if args.log:
    log_level = args.log

    if log_level == 1:
        speci_file_data += "--log-level INFO "

    if log_level == 2:
        speci_file_data += "--log-level WARN "

    if log_level == 3:
        speci_file_data += "--log-level ERROR "

    if log_level == 4:
        speci_file_data += "--log-level CRITICAL "

    if log_level == 5:
        speci_file_data += "--log-level TRACE "

    if log_level == 6:
        speci_file_data += "--log-level DEBUG "
else:
    speci_file_data += "--log-level INFO "

if args.dir:
    speci_file_data += "-D "
else:
    speci_file_data += "-F --noupx "

if args.path:
    file_path = args.path[0]
    if file_exists(file_path):
        if is_file(file_path):
            file_i.set_path(file_path)
            file_ext = file_i.extension().strip()
            if file_ext == ".py":
                if is_readable(file_path):
                    speci_file_data += " {}".format(file_path)
                    if args.specpath:
                        specpath = args.specpath[0]
                        speci_file_data += " --specpath {}".format(specpath)
                    log(
                        "command: {}".format(speci_file_data),
                        app_log_dir_name,
                        app_log_name,
                    )
                    os.system("{}".format(speci_file_data))
                    exit_prog()
                else:
                    e_header = cus(255, 100, 100, "Error:")
                    e_body = cus(
                        255, 255, 255, "File {} is not readable".format(file_path)
                    )
                    e_msg = "{}\t{}".format(e_header, e_body)
                    print("{}".format(e_msg))
                    log("{}".format(e_msg), app_log_dir_name, app_error_log_name)
                    exit_prog(0)
            else:
                e_header = cus(255, 100, 100, "Error:")
                e_body = cus(
                    255, 255, 255, "File {} is not a python file".format(file_path)
                )
                e_msg = "{}\t{}".format(e_header, e_body)
                print("{}".format(e_msg))
                log("{}".format(e_msg), app_log_dir_name, app_error_log_name)
        else:
            e_header = cus(255, 100, 100, "Error:")
            e_body = cus(255, 255, 255, "File path {} is not a file".format(file_path))
            e_msg = "{}\t{}\n".format(e_header, e_body)
            print("{}".format(e_msg))
            log("{}".format(e_msg), app_log_dir_name, app_error_log_name)
            exit_prog(0)
    else:
        e_header = cus(255, 100, 100, "Error:")
        e_body = cus(255, 255, 255, "File path {} does not exist".format(file_path))
        e_msg = "{}\t{}\n".format(e_header, e_body)
        print("{}".format(e_msg))
        log("{}".format(e_msg), app_log_dir_name, app_error_log_name)
        exit_prog(0)

elif args.dialog:
    file_path = open_file_type(file_type)
    if file_path:
        if is_readable(file_path):
            speci_file_data += " {}".format(file_path)
            if args.specpath:
                specpath = args.specpath[0]
                speci_file_data += " --specpath {}".format(specpath)
            log("command: {}".format(speci_file_data), app_log_dir_name, app_log_name)
            os.system("{}".format(speci_file_data))
            exit_prog()
        else:
            e_header = cus(255, 100, 100, "Error:")
            e_body = cus(255, 255, 255, "File {} is not readable".format(file_path))
            e_msg = "{}\t{}\n".format(e_header, e_body)
            print("{}".format(e_msg))
            log("{}".format(e_msg), app_log_dir_name, app_error_log_name)
            exit_prog(0)
else:
    exit_prog(0)
