from doctest import debug
from pickletools import read_bytes8
import sys
import codecs
import base64
from custom_modules.FileValidator import fileExists as fe, isFile as isf
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

cus = cms["custom"]


def encode_input():
    str = input("Enter your input to encode:\t")
    str = codecs.encode(str.encode(), encoding="base64", errors="strict")

    msg = "{}".format(str)
    cmsg = cus(255, 255, 255, msg)
    s_msg = cus(34, 255, 34, "Success:")

    print("{}\t{}\n".format(s_msg, cmsg))
    return str


def decode_input():
    str = input("Enter your encoded input to decode:\t")
    d_str = codecs.decode(
        str,
        encoding="base64",
        errors="strict",
    )

    msg = "{}".format(d_str)
    cmsg = cus(255, 255, 255, msg)
    s_msg = cus(34, 255, 34, "Success:")

    print("{}\t{}\n".format(s_msg, cmsg))
    return str



def encode(arg):
    str = arg
    try:
        encoded = codecs.encode(str.encode(), encoding="base64", errors="strict")
        return {"status":True,"original":arg,"encoded":encoded}
    except Exception as exc:
        print(exc)
        raise Exception({"status":False,"reason":exc})


def decode(arg):
    str = arg
    try:
        d_str = codecs.decode(
            str,
            encoding="base64",
            errors="strict",
        )
        return {"status":True,"original":str,"decoded":d_str}
    except Exception as exc:
        print(exc)
        raise Exception({"status":False,"reason":exc})

