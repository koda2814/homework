"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass

Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""


def cache(times: int) -> int:

    def outer(func):
        count = 0 #amount hom much out func was called
        cache_value = None

        def wrapper(*args, **kwargs):
            nonlocal cache_value #some kind of closures
            nonlocal count
            if count == 0:
                count += 1
                cache_value = func(*args, **kwargs)
                return cache_value
            if count >= times - 1:
                count = 0
                return cache_value
            if count < times:
                count += 1
                return cache_value

        return wrapper

    return outer

