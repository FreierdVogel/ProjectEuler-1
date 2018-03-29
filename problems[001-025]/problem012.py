#! python3
"""The sequence of triangle numbers is generated by adding the natural numbers.
What is the value of the first triangle
number to have over five hundred divisors?"""
from itertools import accumulate
from itertools import count
import sys
from os.path import dirname
sys.path.insert(0, dirname(dirname(__file__)))
from utils import sixn


def n_divisors(n):
    divisors = 1
    for i in sixn(int(n / 2 + 1)):
        x = 0
        while n != 1:
            d, m = divmod(n, i)
            if m:
                break
            else:
                n = d
                x += 1
        else:
            divisors *= (x + 1)
            break
        divisors *= (x + 1)
    return divisors

for i in accumulate(count()):
    if n_divisors(i) > 500:
        print(i)
        break
