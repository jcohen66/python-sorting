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

# Driver
d = Data(200)


start = timeit.timeit()
fib(100)
end = timeit.timeit()
print(end - start)

