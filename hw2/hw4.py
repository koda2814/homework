"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable

CACHE = {}

def cache(func: Callable) -> Callable:
    var = 1
    def wrapper(*args, **kwargs):
        print(var)
        result = func(*args, **kwargs)
        CACHE[f'{len(CACHE)} call of initial one'] = result
        return result
    return wrapper

# @cache
def func(a, b):
    return (a**b)**2

# func(1,2)

def main_func():
    name = 'IVAN'
    def inner_func():
        print('hello', name)
        name = 'dima'
    
    return inner_func


a = main_func()
a()
# test = [1,2,3]

# def f(arg):
#     print(arg)
#     print(test)

# f('hi')

"""So, we can just use decorator @cache before our initial func if we want to cache 
results initial func every time(!!) when we call her, or we can use constuction below
if we want to cache result in one specific cases only when we need it, not every time when we call func().

    cache_func = cache(func)
    res = cache_func(2,3)

    print(res)
    print(CACHE)

OUTPUT:
    64
    {'0 call of initial one': 64}

I preferred first one with decorator, so we cache results every time when we just call func()"""