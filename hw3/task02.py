"""
Here's a not very efficient calculation function that calculates something important::
    
import time
import struct
import random
import hashlib

def slow_calculate(value):
    #Some weird voodoo magic calculations
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import time
import struct
import random
import hashlib
import multiprocessing

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

def fast_calculate(diap):
    with multiprocessing.Pool(25) as p:
        res = p.map(slow_calculate, diap)
        return sum(res)



def main():
    start = time.time()
    print(fast_calculate(range(500)))   # output 1024259
    print(time.time() - start)          # output 48.20191216468811

if __name__ == "__main__":
    main()