"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager

class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return isinstance(exc_value, self.exception)



@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass