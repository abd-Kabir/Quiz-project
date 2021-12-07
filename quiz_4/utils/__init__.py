from os.path import join as join_path
from time import time_ns
from uuid import uuid4


def media_path(file_name):
    return f'/media/uploads/{file_name}'


def process_name(code: str, extension: str):
    return f"{code}.{extension}"


def get_extension(file_name: str):
    return file_name.split(".")[-1]


def unique_code():
    return "%s%s" % (time_ns(), str(uuid4()).replace("-", ""))
