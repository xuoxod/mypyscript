import string
from random import *
from multiprocessing.pool import ThreadPool


def generate_password():
    character = (
        string.ascii_letters
        + string.digits
        + string.ascii_uppercase
        + string.punctuation
        + string.ascii_lowercase
    )
    password = "".join(choice(character) for x in range(randint(11, 35)))
    return password


def generate_password_thread():
    pool = ThreadPool(processes=3)
    async_result = pool.apply_async(generate_password, ())
    return async_result.get()
