import functools
import timeit
from functools import lru_cache

class Data(object):
    def __init__(self, n):
        self.n = n

    @functools.cache
    def ft(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

@lru_cache
def fib(n):
    print(n)
    # base case
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

def f(x):
    '''
    >>> f(10)
    Args: 10
    'Valid input'
    >>> f(-1)
    Traceback (most recent call last):
    ...
    ValueError: Invalid input
    '''
    if x  <= 0:
        raise ValueError("Invalid input")
    print(f"Args: {x}")
    return 'Valid input'

def g(x):
    # assert <condition>, [<error>]
    assert x > 0, "Invalid input"

def lst_one_more(lst1, lst2):
    '''
    This will mutate lst1 so that at index
    'i' lst1[i] = lst2[i] + 1
    lst1 and lst2 should be the same length
    '''
    assert len(lst1) == len(lst2), "Length of lists not the same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1


# Driver
d = Data(200)


start = timeit.timeit()
fib(100)
end = timeit.timeit()
print(end - start)

lst1 = [1]
lst2 = [2]
lst_one_more(lst1, lst2)
for i, x in enumerate(lst1):
    assert x == lst2[i] + 1

