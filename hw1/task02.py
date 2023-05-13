"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence

def check_fibonacci(data: list) -> bool:

    # in case if sequence is empty
    if not data: return False

    # in case if sequence has one element
    if len(data) == 1: 
        return True if data[0] == 0 else False 

    # in case if sequence has of two elements
    if len(data) == 2: 
        if data[0] == 0 and data[1] == 1:
            return True
        else:
            return False

    #in case of sequence has 3 or more elements
    for i in range(1, len(data)): 
        if i + 1 == len(data): return True       #to avoid 'out of range' exception
        if data[i + 1] != data[i] + data[i-1]: 
            return False 
