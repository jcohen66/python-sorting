"""
Uses generators so very efficient
"""

import itertools as it

pows = map(pow, range(10), it.repeat(2))
print(list(pows))

pows = map(pow, range(10), it.repeat(3))
print(list(pows))

pows = map(pow, range(10), it.repeat(4))
print(list(pows))

all_ones = it.repeat(1, times=5)
print(list(all_ones))

"""
Never ending sequence
"""
# alternating_ones = it.cycle([1, -1])
# print(next(alternating_ones)/';;p'-[0p
# print(next(alternating_ones))
# print(next(alternating_ones))
# print(next(alternating_ones))



