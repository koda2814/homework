"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
import itertools


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    '''
    I use list compressions instead loops because it`s faster
    amount - its a boolean list, which contains only 'True' values 
    method product() from itertools gives all possible combinations (with lenght 4) all elemtents from 4 lists
    if sum of elements from some combination equals 0, then we apend 'True' value in 'amount'
    and, finnaly, return lenght of list 'amount' 
    '''

    amount = [True for x in itertools.product(a, b, c, d) if sum(x) == 0]
    return len(amount)
